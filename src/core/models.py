from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class CustomUser(AbstractUser):
    id = models.UUIDField(unique=True, editable=False, default=uuid4, primary_key=True)
    GENDER = [
        ('', ''),
        ('male', 'male'),
        ('female', 'female')
    ]
    BLOOD_GROUP = [
        ('O+', '0+'),
        ('O-', '0-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B+'),
    ]
    
    image = models.ImageField(upload_to='user_images', default='user_image.jpg', blank=True)
    gender = models.CharField(max_length=6, choices=GENDER, blank=True, default=GENDER[1])
    dob = models.DateTimeField(blank=True, null=True)
    blood_group = models.CharField(max_length=2, choices=BLOOD_GROUP, blank=True, default='')
    home_address = models.TextField(blank=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    next_of_kin = models.CharField(max_length=11, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} | @{self.username}"

class DriversLicense(models.Model):
    class Meta:
        ordering = ['-id']

    CLASS = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]
    STATUS = [
        ('approved', 'approved'),
        ('declined', 'declined'),
        ('expired', 'expired'),
        ('pending', 'pending'),
    ]

    id = models.UUIDField(unique=True, editable=False, default=uuid4, primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    assigned_class = models.CharField(max_length=1, choices=CLASS)
    license_number = models.CharField(max_length=20, default='')
    address = models.TextField(default='')
    image = models.ImageField(upload_to='license_images', default='license_images.jpg', blank=True)
    dob = models.DateField(default='1900-10-1')
    iss = models.DateField()
    exp = models.DateField()
    status = models.CharField(choices=STATUS, max_length=10, default='pending')
    timestamp = models.DateTimeField(auto_now=now)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name} | {self.license_number}'
    
    def is_last_item(self):
        if __class__.objects.all().last().id == self.id:
            return True
        return False


class Notice(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='notice_images', default='notice_image.jpg')
    location = models.TextField(help_text="The locality where project is needed")
    tools = models.CharField(max_length=400, help_text='separate tools by using comma(,)')
    description = models.TextField(blank=True)
    Timestamp = models.DateTimeField(auto_now=now)

    def __str__(self) -> str:
        return self.title


class PlateNumber(models.Model):
    STATUS = [
        ('approved', 'approved'),
        ('declined', 'declined'),
        ('expired', 'expired'),
        ('pending', 'pending'),
    ]
    id = models.UUIDField(unique=True, editable=False, default=uuid4, primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    drivers_license = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to='plate_number_owners_passowrds.jpg', default='passports.jpg')
    id_card = models.ImageField(upload_to='id_cards', default='id_card_image.jpg')
    custom_papers = models.ImageField(blank=True)
    delivery_note = models.ImageField(blank=True)
    proof_of_ownership = models.ImageField(blank=True)
    tax_id = models.CharField(max_length=20, unique=True)
    insurance_papers = models.ImageField(blank=True)
    engine_number = models.CharField(max_length=30, unique=True)
    proof_of_address = models.ImageField(help_text='e.g. Utility Bill')
    insurance_policy_number = models.CharField(max_length=20, unique=True)
    issues_date = models.DateField(default='1900-01-01')
    expiry_date = models.DateField(default='1900-01-01')
    status = models.CharField(max_length=10, choices=STATUS)
    model_of_car = models.CharField(max_length=30, blank=True)
    color = models.CharField(max_length=40)
    plate_number = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name} | {self.plate_number}'
    
    def is_empty(self):
        if __class__.objects.all() == []:
            return True
        return False
