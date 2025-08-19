from django.contrib.auth import get_user_model
from rest_framework import serializers

# Get current user model
User = get_user_model()


class UserRegistrationSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11)
    email = serializers.EmailField()
    full_name = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True)

    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError(
                "User with this phone number already exists"
            )
        return value


class VerifyCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=7)


class UserLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11)
    password = serializers.CharField()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("phone_number", "email", "full_name")
