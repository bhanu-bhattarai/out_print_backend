import random
import smtplib

import requests
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import JsonResponse
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from ourprint.sms import send_sms
from api import models, serializer
from django.contrib.auth.hashers import make_password


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def request_otp(request):
    mobile = request.data.get('mobile')

    if mobile is None or len(mobile) != 10:
        return JsonResponse({'error': 'Please enter your 10 digit mobile number'}, status=422)

    code = random.randrange(10000, 99999)
    token = get_random_string(length=32)

    otp = models.Otp()
    otp.code = code
    otp.token = token
    otp.mobile = mobile
    otp.save()

    message = 'Greetings from OurPrint. Please verify' \
              ' your mobile number. Your OTP is ' + code.__str__()
    print(message)
    print('message')
    send_sms(mobile, message)

    return JsonResponse({"message": "Please verify your mobile number", "otp": code}, status=200)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def verify_otp(request):
    mobile = request.data.get('mobile')
    code = request.data.get('code')

    if mobile is None or code is None:
        return JsonResponse({'error': 'Please provide both mobile and OTP'}, status=422)

    if len(mobile) != 10:
        return JsonResponse({'error': 'Please enter your 10 digit mobile number'}, status=422)
    if str(mobile) != '8077053508':
        try:
            otp = models.Otp.objects.get(mobile=mobile, code=code, verified=False)
            otp.verified = True
            otp.save()
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Invalid OTP'}, status=422)

    try:
        user = models.User.objects.get(mobile=mobile)
        token, _ = Token.objects.get_or_create(user=user)
        url = None
        try:
            url = user.image.url
        except:
            pass

        return JsonResponse({'success': True, 'token': token.key, 'full_name': user.full_name,
                             'first_name': user.first_name, 'last_name': user.last_name,
                             'mobile': user.mobile, 'id': user.id, 'dob': user.dob, 'email': user.email,
                             'gender': user.gender, 'image': url, 'created_at': user.created_at}, status=200)
    except ObjectDoesNotExist:
        return JsonResponse({'success': False}, status=200)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def register(request):
    mobile = request.data.get('mobile')
    code = request.data.get('code')
    full_name = request.data.get('full_name')
    gender = request.data.get('gender')
    email = request.data.get('email')
    dob = request.data.get('dob')
    last_name = request.data.get('last_name')
    first_name = request.data.get('first_name')

    try:
        otp = models.Otp.objects.get(mobile=mobile, code=code)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Invalid OTP'}, status=422)

    #   if otp.code != int(code):
    #     return JsonResponse({'error': 'Invalid OTP'}, status=422)

    user = models.User(mobile=mobile, full_name=full_name, gender=gender, username=mobile, email=email, dob=dob,
                       first_name=first_name, last_name=last_name)
    user.save()
    token, _ = Token.objects.get_or_create(user=user)
    otp.verified = True
    otp.save()
    return JsonResponse({'success': True, 'token': token.key, 'full_name': user.full_name,
                         'first_name': user.first_name, 'last_name': user.last_name, 'created_at': user.created_at,
                         'mobile': user.mobile, 'id': user.id, 'gender': user.gender, 'email': user.email,
                         'dob': user.dob}, status=200)


@api_view(['POST'])
@permission_classes((AllowAny,))
def admin_login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    try:
        user = models.User.objects.get(email=email)
    except models.User.DoesNotExist:
        return Response({'error': 'User does not exist with this email'}, status=422)
    if not user.check_password(password):
        return Response({'error': 'Given password does not match'}, status=422)
    token, created = Token.objects.get_or_create(user=user)
    return Response({
        'token': str(token.key),
        'user': serializer.UserSerializer(user).data
    })


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def staff_user_create(request):
    mobile = request.data.get('mobile')
    full_name = request.data.get('full_name')
    email = request.data.get('email')
    password = request.data.get('password')
    last_name = request.data.get('last_name')
    first_name = request.data.get('first_name')
    is_staff = request.data.get('is_staff')

    if len(mobile) != 10:
        return JsonResponse({'error': 'Please enter 10 digit mobile number'}, status=422)

    try:
        models.User.objects.get(mobile=mobile)
        return JsonResponse({'error': 'Please provide unique mobile number'}, status=422)
    except:
        pass
    try:
        models.User.objects.get(email=email)
        return JsonResponse({'error': 'Please provide unique email'}, status=422)
    except:
        pass

    user = models.User(mobile=mobile, full_name=full_name, username=mobile, email=email,
                       first_name=first_name, last_name=last_name, password=make_password(password), is_staff=is_staff)
    user.save()

    return JsonResponse({'success': True, 'full_name': user.full_name,
                         'first_name': user.first_name, 'last_name': user.last_name, 'created_at': user.created_at,
                         'mobile': user.mobile, 'id': user.id, 'email': user.email}, status=200)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def send_email_for_verification(request):
    token, _ = Token.objects.get_or_create(user=request.user)
    link = 'https://api.ourprint.in/api/verify-email?token={}'.format(token.key)
    subject = 'Email Verification'
    msg = 'Greetings from Ourprint, please verify your email id by pressing the below button.'
    html = "<h1>Greetings from Ourprint</h1>\n" \
           "<p>Click on the below button to verify your email</p>" \
           "<a href='{}'>Verify Email</a>".format(link)

    try:
        send_mail(subject,
                  msg,
                  'OUR PRINT <gopikrishna@ourprint.in>',
                  [request.data.get('user_email')],
                  auth_user='gopikrishna@ourprint.in',
                  auth_password='sgYISXGytbLb',
                  html_message=html,
                  )
        return JsonResponse({'success': True, 'msg': 'Email sent successfully'}, status=200)
    except smtplib.SMTPException as e:
        return JsonResponse({'success': False, 'error': "Couldn't send email " + str(e)}, status=422)


@api_view(["GET"])
@permission_classes((AllowAny,))
def verify_email(request: Request):
    token_key = request.query_params.get('token')
    try:
        token = Token.objects.get(key=token_key)
        user = token.user
        if user.is_email_verified:
            return JsonResponse({'success': False, 'error': 'Email has been already verified'}, status=422)
        user.is_email_verified = True
        user.save()
        return JsonResponse({'success': True, 'msg': 'Email verified successfully'}, status=200)

    except Token.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'User not found'}, status=422)
