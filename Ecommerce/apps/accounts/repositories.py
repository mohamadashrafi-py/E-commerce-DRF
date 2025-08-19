from django.contrib.auth import authenticate
from django.db import transaction
from rest_framework.authtoken.models import Token

from .models import OtpCodeModel, User


class UserRepository:
    @staticmethod
    @transaction.atomic
    def create_user(phone_number, email, full_name, password):
        user = User.objects.create_user(
            phone_number=phone_number,
            email=email,
            full_name=full_name,
            password=password,
        )
        return user

    @staticmethod
    def get_user_by_phone(phone_number):
        try:
            return User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            return None

    @staticmethod
    def authenticate_user(phone_number, password):
        return authenticate(phone_number=phone_number, password=password)


class OtpCodeRepository:
    @staticmethod
    def create_otp_code(phone_number, code):
        # Delete any existing OTP for this phone number
        OtpCodeModel.objects.filter(phone_number=phone_number).delete()
        return OtpCodeModel.objects.create(phone_number=phone_number, code=code)

    @staticmethod
    def get_otp_code(phone_number):
        try:
            return OtpCodeModel.objects.get(phone_number=phone_number)
        except OtpCodeModel.DoesNotExist:
            return None

    @staticmethod
    def delete_otp_code(phone_number):
        OtpCodeModel.objects.filter(phone_number=phone_number).delete()


class TokenRepository:
    @staticmethod
    def create_token(user):
        token, created = Token.objects.get_or_create(user=user)
        return token

    @staticmethod
    def delete_token(user):
        Token.objects.filter(user=user).delete()

    @staticmethod
    def get_user_from_token(token_key):
        try:
            token = Token.objects.get(key=token_key)
            return token.user
        except Token.DoesNotExist:
            return None
