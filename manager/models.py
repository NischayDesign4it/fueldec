from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email


class vehicle(models.Model):
    vehicleNumber = models.CharField(max_length=50, unique=True)
    vehicleId = models.CharField(max_length=50, unique=True)
    quantity = models.IntegerField(null=True)
    gallonLimit = models.IntegerField(null=True,default=0)
    odometer = models.IntegerField(null=True)
    companyName = models.CharField(null=False, max_length=50)
    productName = models.CharField(null=False, max_length=50)
    totalGallon = models.IntegerField(null=True,default=0)
    meteredHours = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.vehicleNumber

class transactions(models.Model):
    id = models.AutoField(primary_key=True)
    vehicleNumber = models.CharField(max_length=50)
  #  vehicleId = models.CharField(max_length=50, unique=True)
    gallonLimit = models.IntegerField(null=True)
    dispensedQuantity = models.IntegerField(null=True)

    odometer = models.IntegerField(null=True)
    totalGallon = models.IntegerField(null=True)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.vehicleNumber

class pumpInfo(models.Model):
    id = models.AutoField(primary_key=True)
    pumpNumber = models.CharField(max_length=20)
    vehicleNumber = models.CharField(max_length=50, null=True)
    odometer = models.IntegerField(null=True)
    pumpStatus = models.BooleanField(default=False)

    def __str__(self):
        return self.pumpNumber