from django.http import JsonResponse, HttpResponse
from rest_framework import serializers
from api import models
from django.db.models import Value, BooleanField, Q
from rest_framework.response import Response


class OrdersSerializer(serializers.ModelSerializer):
    user_data = serializers.SerializerMethodField()
    assigned_user_data = serializers.SerializerMethodField()
    address_data = serializers.SerializerMethodField()

    class Meta:
        model = models.Order
        fields = '__all__'

    def get_user_data(self, obj):
        if obj.user is None:
            return None
        return UserSerializer(obj.user).data

    def get_assigned_user_data(self, obj):
        if obj.assigned_user is None:
            return None
        return UserSerializer(obj.assigned_user).data

    def get_address_data(self, obj):
        if obj.address is None:
            return None
        return AddressesSerializer(obj.address).data


# class AssignedOrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.AssignedOrder
#         fields = '__all__'


class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'


class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Configuration
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()

    class Meta:
        model = models.User
        fields = ['id', 'full_name', 'mobile', 'gender', 'dob', 'email',
                  'image', 'course', 'is_student', 'branch',
                  'year', 'sem', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'created_at',
                  'is_email_verified',
                  'occupation', 'college_name', 'address']

    def get_address(self, obj):
        if obj.id is None:
            return None
        return AddressesSerializer(models.Address.objects.filter(user=obj.id), many=True,
                                   context=self.context).data


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderStatus
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    assigned_orders = serializers.SerializerMethodField()

    class Meta:
        model = models.User
        fields = ['id', 'full_name', 'mobile', 'gender', 'dob', 'email',
                  'image', 'course', 'is_student', 'branch',
                  'year', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'created_at', 'is_email_verified',
                  'occupation', 'assigned_orders']

    def get_assigned_orders(self, obj):
        if obj.id is None:
            return None
        orders = models.Order.objects.filter(~Q(status='out_for_delivery'), ~Q(status='delivered'),
                                             is_payment_complete=True,
                                             assigned_user=obj.id).count()
        return orders


class PinCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PinCode
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.State
        fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = '__all__'


class ConnectWithUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ConnectWithUs
        fields = '__all__'

class QrCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QrCode
        fields = '__all__'


class UserQrOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserQrOrder
        fields = '__all__'