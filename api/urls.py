from django.urls import path
from rest_framework import routers

from api import views, user_views

router = routers.DefaultRouter()
router.register('orders', views.OrdersViewSet),
router.register('pin_code', views.PinCodeViewSet),
router.register('order_status', views.OrderStatusViewSet),
router.register('addresses', views.AddressesViewSet),
router.register('configurations', views.ConfigurationViewSet),
router.register('users', views.UserViewSet),
router.register('staff_users', views.StaffViewSet)
router.register('my_orders', views.MyOrdersViewSet)
router.register('states', views.StateViewSet)
router.register('contact_us', views.ContactUsViewSet)
router.register('connect_with_us', views.ConnectWithUsViewSet)

# router.register('assigned-orders', views.AssignedOrderViewSet)

urlpatterns = router.urls + [
    path('profile/', views.ProfileViewSet.as_view()),
    path('request-otp/', user_views.request_otp),
    path('verify-otp/', user_views.verify_otp),
    path('register/', user_views.register),
    path('send-email-for-verification/', user_views.send_email_for_verification),
    path('verify-email', user_views.verify_email),
    path('is-freemium/', views.is_freemium_available),
    path('get-delivery-charges/', views.get_delivery_charges),
    path('get-spiral-binding-charges/', views.get_spiral_binding_charges),
    path('admin-login', user_views.admin_login),
    path('update_password', views.change_password),
    path('dashboard/', views.dashboard),
    path('staff-dashboard/', views.staff_dashboard),
    path('staff_users_create/', user_views.staff_user_create),
    path('verify-payment/', views.verify_payment),
    path('get-qr-codes/', views.get_qr_code),
    path('save-qr-codes/', views.save_qr_code),
    path('delete-qr-codes/<str:pk>/', views.delete_qr_code),
    path('update-qr-codes/<str:pk>/', views.update_qr_code),
    path('scan-qr-code/', views.scan_qr_code),
]
