import datetime
from django.db.models import Q

from django.db.models import Value, BooleanField, Q
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.shortcuts import render
from razorpay.errors import BadRequestError
from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from api import models, serializer
import calendar
from django.db.models import Sum
import pytz
from django.core import serializers
from django.db.models import Max

# Create your views here.
from api.models import OrderStatus
from api.serializer import OrderStatusSerializer
from api.serializer import QrCodeSerializer
import razorpay


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializer.UserSerializer

    def get_queryset(self):
        return models.User.objects.filter(~Q(is_superuser=True), ~Q(is_staff=True))

    pagination_class = None


class ProfileViewSet(generics.RetrieveUpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializer.UserSerializer

    def get_object(self):
        instance = models.User.objects.get(pk=self.request.user.id)
        return instance

    def get(self, request, *args, **kwargs):
        user = models.User.objects.get(pk=request.user.id)
        user_serializer = serializer.UserSerializer(user, many=False, context={"request": request})
        return Response(user_serializer.data)

    # def put(self, request, *args, **kwargs):
    #     user = User.objects.get(pk=request.user.id)
    #
    #     serializer = UserSerializer(user, data=request.data, context={"request": request})
    #     if serializer.is_valid():
    #         serializer.update(user, request.data)
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=400)


@api_view(['POST'])
@permission_classes((AllowAny,))
def change_password(request):
    given_password = request.data.get('password')
    given_old_password = request.data.get('old_password')
    # print(given_old_password)
    user = models.User.objects.get(pk=request.user.id)
    print(user.password)

    if not user.check_password(given_old_password):
        return Response({
            'message': 'Please enter the correct password'
        }, status=400)

    user.password = make_password(given_password)
    user.save()
    return Response({
        'message': 'Your password has been successfully changed'
    }, status=200)


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializer.OrdersSerializer

    pagination_class = None

    def perform_create(self, serializer):

        max = models.Order.objects.aggregate(id_max=Max('id'))['id_max']
        order_id = "{}{:05d}".format('OPAA', max + 1 if max is not None else 1)
        serializer.save(order_id=order_id)

    def get_queryset(self):
        user = self.request.query_params.get('user')
        is_freemium = self.request.query_params.get('is_freemium')
        exclude_status = self.request.query_params.get('exclude_status')
        status_exclude = self.request.query_params.get('status_exclude')
        status = self.request.query_params.get('status')
        from_date = self.request.query_params.get('from_date')
        to_date = self.request.query_params.get('to_date')
        is_payment_complete = self.request.query_params.get('is_payment_complete')

        print(status)
        filters = {'is_payment_complete': True}
        if is_payment_complete:
            filters['is_payment_complete'] = is_payment_complete

        if user:
            filters['user'] = user
        if status:
            filters['status'] = status

        if is_freemium:
            filters['is_freemium'] = is_freemium

        if from_date and to_date:
            filters['updated_at__gte'] = from_date
            filters['updated_at__lte'] = to_date

        if exclude_status:
            return models.Order.objects.filter(~Q(status=exclude_status), **filters)
        if status_exclude:
            return models.Order.objects.filter(~Q(status='delivered') & ~Q(status='confirmed'), **filters)
        else:
            return models.Order.objects.filter(**filters)


# class AssignedOrderViewSet(viewsets.ModelViewSet):
#     queryset = models.AssignedOrder.objects.all()
#     serializer_class = serializer.AssignedOrderSerializer

class StaffViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.StaffSerializer
    queryset = models.User.objects.filter(is_staff=True, is_superuser=False)

    def perform_update(self, serializer):
        if self.request.data.get('password') is None:
            return None
        given_password = self.request.data.get('password')
        password = make_password(given_password)
        serializer.save(password=password)

    pagination_class = None


class MyOrdersViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.OrdersSerializer
    queryset = models.Order.objects.all()

    def get_queryset(self):
        exclude_status = self.request.query_params.get('exclude_status')
        status = self.request.query_params.get('status')
        assigned_user = self.request.query_params.get('assigned_user')
        from_date = self.request.query_params.get('from_date')
        to_date = self.request.query_params.get('to_date')

        filters = {'is_payment_complete': True}
        if status:
            filters['status'] = status
        if assigned_user:
            filters['assigned_user'] = assigned_user
        if from_date:
            filters['updated_at__gte'] = from_date
        if to_date:
            filters['updated_at__lte'] = to_date
        if exclude_status:
            return models.Order.objects.filter(~Q(status=exclude_status), **filters)
        else:
            return models.Order.objects.filter(**filters)

    pagination_class = None


class AddressesViewSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializer.AddressesSerializer

    def get_queryset(self):
        user = self.request.query_params.get('user')
        filters = {}
        if user:
            filters['user'] = user

        return models.Address.objects.filter(**filters)


class ConfigurationViewSet(viewsets.ModelViewSet):
    queryset = models.Configuration.objects.all()
    serializer_class = serializer.ConfigurationSerializer
    pagination_class = None


class OrderStatusViewSet(viewsets.ModelViewSet):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer
    pagination_class = None

    def get_queryset(self):
        status = self.request.query_params.get('status')
        order = self.request.query_params.get('order')
        filters = {}
        if status:
            filters['status'] = status
        if order:
            filters['order'] = order

        return models.OrderStatus.objects.filter(**filters)


class PinCodeViewSet(viewsets.ModelViewSet):
    queryset = models.PinCode.objects.all()
    serializer_class = serializer.PinCodeSerializer
    pagination_class = None


class StateViewSet(viewsets.ModelViewSet):
    queryset = models.State.objects.all()
    serializer_class = serializer.StateSerializer
    pagination_class = None


@api_view(["GET"])
def is_freemium_available(request):
    user = request.user
    today = datetime.date.today()
    is_freemium_available = models.Order.objects.filter(user=user.id, is_freemium=True,
                                                        created_at__year=today.year,
                                                        created_at__month=today.month,
                                                        is_payment_complete=True).exists()
    return JsonResponse({'is_freemium_available': not is_freemium_available}, status=200)


@api_view(["GET"])
def dashboard(request):
    from_date = request.query_params.get('from_date')
    to_date = request.query_params.get('to_date')

    filters = {}
    newfilters = {}
    if from_date and to_date:
        newfilters['updated_at__gte'] = from_date
        newfilters['updated_at__lte'] = to_date
        filters['created_at__gte'] = from_date
        filters['created_at__lte'] = to_date
    completed_orders = models.Order.objects.filter(is_payment_complete=True, status='delivered', **newfilters).count()
    orders = models.Order.objects.filter(is_payment_complete=True, **filters).count()
    total_pages = models.Order.objects.filter(is_payment_complete=True, status='delivered', **filters).aggregate(
        Sum('pdf_page_count'))['pdf_page_count__sum']
    total_amount = \
        models.Order.objects.filter(is_payment_complete=True, status='delivered', **filters).aggregate(Sum('amount'))[
            'amount__sum'] + \
        models.Order.objects.filter(is_payment_complete=True, status='delivered', **filters).aggregate(
            Sum('delivery_charge'))[
            'delivery_charge__sum']
    students = models.User.objects.filter(is_student=True, **filters).count()
    non_students = models.User.objects.filter(is_student=False, **filters).count()
    total_users = models.User.objects.all().count()
    freemium = models.Order.objects.filter(is_payment_complete=True, order_type='freemium', **filters).count()
    standard = models.Order.objects.filter(is_payment_complete=True, order_type='standard_print', **filters).count()
    official = models.Order.objects.filter(is_payment_complete=True, order_type='official_documents', **filters).count()

    return JsonResponse({
        'students': students,
        'non_students': non_students,
        'completed_orders': completed_orders,
        'total_users': total_users,
        'orders': orders,
        'freemium': freemium,
        'standard': standard,
        'official': official,
        'total_pages': total_pages,
        'total_amount': total_amount
    }, status=200)


@api_view(["GET"])
def staff_dashboard(request):
    print(request)
    from_date = request.query_params.get('from_date')
    to_date = request.query_params.get('to_date')
    staff_id = request.query_params.get('staff_id')

    filters = {}
    new_filters = {}
    if from_date:
        filters['created_at__gte'] = from_date
        new_filters['updated_at__gte'] = from_date
    if to_date:
        filters['created_at__lte'] = to_date
        new_filters['updated_at__lte'] = to_date
    if staff_id:
        filters['user'] = staff_id
        new_filters['assigned_user'] = staff_id

    completed_orders = models.OrderStatus.objects.filter(order__is_payment_complete=True, status='delivered',
                                                         **filters).count()
    assigned_orders = models.OrderStatus.objects.filter(order__is_payment_complete=True, status='assigned',
                                                        **filters).count()
    processing_orders = models.OrderStatus.objects.filter(order__is_payment_complete=True, status='processing',
                                                          **filters).count()
    freemium = models.Order.objects.filter(is_payment_complete=True, order_type='freemium',
                                           **new_filters).count()
    standard = models.Order.objects.filter(is_payment_complete=True, order_type='standard_print',
                                           **new_filters).count()
    official = models.Order.objects.filter(is_payment_complete=True, order_type='official_documents',
                                           **new_filters).count()
    return JsonResponse({
        'assigned_orders': assigned_orders,
        'processing_orders': processing_orders,
        'completed_orders': completed_orders,
        'freemium': freemium,
        'standard': standard,
        'official': official
    }, status=200)


@api_view(["POST"])
def get_delivery_charges(request):
    pdf_count = request.data.get('order_details')['pdf_page_count']
    address_id = request.data.get('order_details')['address']
    address = models.Address.objects.get(id=address_id)

    if models.PinCode.objects.filter(Q(city='Hyderabad') | Q(city='Rangareddy'), pin_code=address.pin_code).exists():
        delivery_charges = 30
    else:
        delivery_charges = 40

    print(pdf_count)

    if pdf_count > 250:
        charges = pdf_count / 250
        whole_charges = int(pdf_count / 250)
        if charges > whole_charges:
            delivery_charges += whole_charges * 10
        else:
            delivery_charges += (whole_charges - 1) * 10
        print(whole_charges)

    return JsonResponse({'charges': delivery_charges})


@api_view(["POST"])
def get_spiral_binding_charges(request):
    pdf_count = request.data.get('pdf_page_count')
    spiral_binding_charge = request.data.get('spiral_binding_charge')
    print(pdf_count)
    charges = pdf_count / 150
    print(charges)
    if pdf_count % 150 == 0:
        final_charge = charges * spiral_binding_charge
    else:
        final_charge = int(charges + 1) * spiral_binding_charge

    return JsonResponse({'charges': final_charge})


@api_view(["POST"])
def verify_payment(request):
    payment_id = request.data.get('payment_id')
    order_id = request.data.get('order_id')
    client = razorpay.Client(auth=("rzp_live_2hHxvmoZPbKYDz", "xbqrAYm8PXoLb7Qom6R6dUGQ"))
    try:
        resp = client.payment.fetch(payment_id)
        print(resp)
        if resp and resp['error_code'] is None:
            if resp['notes']['order_id'] == order_id:
                capture_res = client.payment.capture(payment_id, resp['amount'])
                models.Order.objects.filter(pk=order_id).update(is_payment_complete=True)
                return JsonResponse({'status': 'Successful', 'code': 0}, status=200)
    except BadRequestError as e:
        print(e)
        return JsonResponse({'error': e.__str__()}, status=422)

    return JsonResponse({'status': 'Failed', 'code': 1}, status=422)


@permission_classes((AllowAny,))
class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = models.ContactUs.objects.all()
    serializer_class = serializer.ContactUsSerializer
    pagination_class = None


@permission_classes((AllowAny,))
class ConnectWithUsViewSet(viewsets.ModelViewSet):
    queryset = models.ConnectWithUs.objects.all()
    serializer_class = serializer.ConnectWithUsSerializer
    pagination_class = None

@api_view(["GET"])
def get_qr_code(request):
    qrCode = models.QrCode.objects.all()
    serializer_qr = QrCodeSerializer(qrCode, many = True)
    return Response(serializer_qr.data, status = 200)

@api_view(["POST"])
def save_qr_code(request):
    serializer_qr = QrCodeSerializer(data=request.data)
    if serializer_qr.is_valid():
        serializer_qr.save()
        return Response( "Successful", status = 201)
    return Response("failure", status=400)
