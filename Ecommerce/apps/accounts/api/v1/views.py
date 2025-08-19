from django.core.cache import cache
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Ecommerce.apps.accounts.services import AuthService

from .serializers import (UserLoginSerializer, UserProfileSerializer,
                          UserRegistrationSerializer, VerifyCodeSerializer)


class UserRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user_data, error = AuthService.register_user(
            phone_number=serializer.validated_data["phone_number"],
            email=serializer.validated_data["email"],
            full_name=serializer.validated_data["full_name"],
            password=serializer.validated_data["password"],
        )

        if error:
            return Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)

        # Store user data in cache for verification (expires in 10 minutes)
        cache_key = f"registration_{user_data['phone_number']}"
        cache.set(cache_key, user_data, timeout=600)

        return Response(
            {
                "message": "OTP code sent successfully",
                "phone_number": user_data["phone_number"],
            },
            status=status.HTTP_200_OK,
        )


class UserRegisterVerifyCodeView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = VerifyCodeSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        phone_number = request.data.get("phone_number")
        code = serializer.validated_data["code"]

        # Get user data from cache
        cache_key = f"registration_{phone_number}"
        user_data = cache.get(cache_key)

        if not user_data:
            return Response(
                {"error": "Registration session expired or invalid"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        result, error = AuthService.verify_otp_and_create_user(
            phone_number, code, user_data
        )

        if error:
            return Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)

        # Remove user data from cache
        cache.delete(cache_key)

        return Response(
            {
                "message": "User registered successfully",
                "token": result["token"],
                "user": UserProfileSerializer(result["user"]).data,
            },
            status=status.HTTP_201_CREATED,
        )


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        result, error = AuthService.login_user(
            phone_number=serializer.validated_data["phone_number"],
            password=serializer.validated_data["password"],
            request=request,
        )

        if error:
            return Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            {
                "message": "Login successful",
                "token": result["token"],
                "user": UserProfileSerializer(result["user"]).data,
            },
            status=status.HTTP_200_OK,
        )


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        _, error = AuthService.logout_user(request.user, request)

        if error:
            return Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
