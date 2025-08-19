import random

from django.contrib.auth import login, logout

from Ecommerce.common.common import send_otp_code

from .repositories import OtpCodeRepository, TokenRepository, UserRepository


class AuthService:
    @staticmethod
    def generate_otp_code():
        return random.randint(1000000, 9999999)

    @staticmethod
    def register_user(phone_number, email, full_name, password):
        # Check if user already exists
        if UserRepository.get_user_by_phone(phone_number):
            return None, "User with this phone number already exists"

        # Generate OTP code
        otp_code = AuthService.generate_otp_code()

        # Send OTP code
        send_otp_code(phone_number, otp_code)

        # Create OTP record
        OtpCodeRepository.create_otp_code(phone_number, otp_code)

        # Store user data temporarily
        user_data = {
            "phone_number": phone_number,
            "email": email,
            "full_name": full_name,
            "password": password,
        }

        return user_data, None

    @staticmethod
    def verify_otp_and_create_user(phone_number, code, user_data):
        # Get OTP code
        otp_instance = OtpCodeRepository.get_otp_code(phone_number)

        if not otp_instance:
            return None, "OTP code not found"

        if str(otp_instance.code) != str(code):
            return None, "Invalid OTP code"

        if not otp_instance.is_valid:
            return None, "Expired OTP code"

        # Create user
        try:
            user = UserRepository.create_user(
                phone_number=user_data["phone_number"],
                email=user_data["email"],
                full_name=user_data["full_name"],
                password=user_data["password"],
            )
        except Exception as e:
            return None, f"Error creating user: {str(e)}"

        # Delete OTP code
        OtpCodeRepository.delete_otp_code(phone_number)

        # Create token
        token = TokenRepository.create_token(user)

        return {"user": user, "token": token.key}, None

    @staticmethod
    def login_user(phone_number, password, request=None):
        user = UserRepository.authenticate_user(phone_number, password)

        if not user:
            return None, "Invalid phone number or password"

        if not user.is_active:
            return None, "User account is disabled"

        # Create or get token
        token = TokenRepository.create_token(user)

        # Login user (for session authentication)
        if request:
            login(request, user)

        return {"user": user, "token": token.key}, None

    @staticmethod
    def logout_user(user, request=None):
        # Delete token
        TokenRepository.delete_token(user)

        # Logout user (for session authentication)
        if request:
            logout(request)

        return True, None
