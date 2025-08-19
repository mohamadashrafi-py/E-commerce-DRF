import datetime

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from . import managers


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    full_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = managers.UserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["full_name"]

    def __str__(self):
        return f"{self.full_name} - {self.phone_number} - {self.email}"

    @property
    def is_staff(self):
        return self.is_admin


class OtpCodeModel(models.Model):
    phone_number = models.CharField(max_length=11, unique=True)
    code = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"{self.phone_number} - {self.code} - {self.created}"

    @property
    def is_valid(self):
        """Check if OTP code is still valid (within 60 seconds of creation)"""
        if not self.created:
            return False
        expiration_time = self.created + datetime.timedelta(seconds=60)
        return timezone.now() < expiration_time
