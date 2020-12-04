from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
from django.utils import timezone
from django.db.models import Max


class User(AbstractUser):
    GENDERS = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    )
    YEAR = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    SEM = (
        (1, 1),
        (2, 2),
    )
    full_name = models.CharField(max_length=60, blank=True, default="", null=True)
    first_name = models.CharField(max_length=60, blank=True, default='')
    last_name = models.CharField(max_length=60, blank=True, default='')
    mobile = models.CharField(max_length=10, unique=True)
    gender = models.CharField(max_length=20, null=True, blank=True, choices=GENDERS)
    dob = models.DateTimeField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    course = models.CharField(max_length=50, null=True)
    branch = models.CharField(max_length=50, null=True)
    year = models.IntegerField(null=True, choices=YEAR)
    sem = models.IntegerField(null=True, choices=SEM)
    is_student = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_email_verified = models.BooleanField(default=False, null=True)
    occupation = models.CharField(max_length=100, null=True)
    college_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.full_name)

    class Meta:
        db_table = 'users'
        ordering = ['-created_at']


class Otp(models.Model):
    code = models.IntegerField()
    mobile = models.CharField(max_length=10)
    token = models.CharField(max_length=255)
    verified = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "otp"


class Configuration(models.Model):
    TYPES = (
        ('print', 'Print'),
        ('binding', 'Binding'),
        ('page', 'Page'),
        ('paper', 'Paper'),
        ('others', 'Others'),
    )
    PRICE_TYPE = (
        ('fixed', 'Fixed'),
        ('dynamic', 'Dynamic'),
        ('per_page', 'Per Page')
    )
    title = models.CharField(max_length=30)
    type = models.CharField(choices=TYPES, max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_type = models.CharField(choices=PRICE_TYPE, max_length=20)
    strike_price = models.DecimalField(max_digits=10, decimal_places=2)
    per_page_count = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'configurations'

    def __str__(self):
        return self.title


class Order(models.Model):
    STATUS = (
        ('incomplete', 'Incomplete'),
        ('confirmed', 'Confirmed'),
        ('assigned', 'Assigned'),
        ('processing', 'Processing'),
        ('departed', 'Departed'),
        ('out-for-delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
    )
    PAGE_CONFIG = (
        ('one-sided', 'One-Sided'),
        ('two-sided', 'Two-Sided'),
    )
    ORDER_TYPE = (
        ('freemium', 'Freemium'),
        ('standard_print', 'Standard Print'),
        ('official_documents', 'Official Documents'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_id = models.CharField(unique=True, null=True, editable=False, max_length=10)
    amount = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=10)
    pdf = models.FileField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    notes = models.CharField(max_length=255, null=True, blank=True)
    address = models.ForeignKey('Address', on_delete=models.CASCADE, related_name='delivery_address', null=True)
    multi_color_notes = models.CharField(max_length=255, null=True, blank=True)
    front_cover_pdf = models.FileField(null=True, blank=True)
    front_cover_pdf_info = models.CharField(max_length=255, null=True, blank=True)
    configurations = models.ManyToManyField(Configuration, related_name='orders', blank=True)
    delivery_charge = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=0)
    price_list = models.CharField(max_length=200, null=True, blank=True)
    config_list = models.TextField(null=True, blank=True)
    pdf_page_count = models.PositiveIntegerField(null=True, blank=True)
    status = models.CharField(choices=STATUS, default='confirmed', max_length=20, auto_created=True)
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    file_name = models.CharField(null=True, blank=True, max_length=256)
    is_freemium = models.BooleanField(default=False)
    page_config = models.CharField(max_length=20, choices=PAGE_CONFIG, default='one-sided')
    delivery_id = models.CharField(max_length=30, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None, blank=True)
    is_payment_complete = models.BooleanField(default=False, null=True)
    order_type = models.CharField(choices=ORDER_TYPE, null=True, max_length=20)

    class Meta:
        db_table = "orders"
        ordering = ['-created_at']


class OrderStatus(models.Model):
    status = (
        ('confirmed', 'Confirmed'),
        ('assigned', 'Assigned'),
        ('processing', 'Processing'),
        ('out-for-delivery', 'Out for Delivery'),
        ('delivered', 'Delivered')
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_statuses')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'order_status'


class Address(models.Model):
    TYPES = (
        ('home', 'Home'),
        ('work', 'Work'),
        ('others', 'Others')
    )
    address_line1 = models.CharField(max_length=255, null=True, blank=True)
    address_line2 = models.CharField(max_length=255, null=True, blank=True)
    landmark = models.CharField(max_length=255, null=True, blank=True)
    pin_code = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True, choices=TYPES)
    alternate_number = models.CharField(max_length=10, null=True, blank=True)
    address_name = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')

    class Meta:
        db_table = 'addresses'

    def __str__(self):
        return self.address_line1


class PinCode(models.Model):
    pin_code = models.CharField(null=True, blank=True, max_length=20)
    city = models.CharField(null=True, max_length=50)

    class Meta:
        db_table = 'pin_codes'


class State(models.Model):
    state = models.CharField(null=True, blank=True, max_length=20)

    class Meta:
        db_table = 'states'


class ContactUs(models.Model):
    full_name = models.CharField(max_length=60, blank=True, default="", null=True)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=50, null=True, blank=True)
    details_of_enquiry = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'contact_us'
        ordering = ['-created_at']


class ConnectWithUs(models.Model):
    full_name = models.CharField(max_length=60, blank=True, default="", null=True)
    company_name = models.CharField(max_length=60, blank=True, default="", null=True)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'connect_with_us'


class QrCode(models.Model):
    code = models.IntegerField()
    generated_date = models.DateTimeField(auto_now_add=True)
    value = models.CharField(max_length=60, blank=True, default="", null=True)
    validity = models.DateTimeField(max_length=30, null=True, blank=True)
    company = models.CharField(max_length=60, blank=True, default="", null=True)
    count = models.CharField(max_length=60, blank=True, default="", null=True)
    image = models.CharField(max_length=60, blank=True, default="", null=True)
    redirection_url = models.CharField(max_length=60, blank=True, default="", null=True)
    is_active = models.BooleanField(default=True, null=True)

    class Meta:
        db_table = 'qr_code'

class UserQrOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    qr_code = models.ForeignKey(QrCode, on_delete=models.CASCADE)
    is_scanned = models.BooleanField(default=False, null=True)
    
    class Meta:
        db_table = 'user_qr_order'