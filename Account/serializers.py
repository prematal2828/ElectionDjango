from rest_framework import serializers
from Account.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = '__all__'


class UserLogInSerializer(serializers.Serializer):
    # class Meta(object):
    #     model = UserAccount
    #     fields = ['phone', 'password']

    phone = serializers.CharField(max_length=11)
    password = serializers.CharField(max_length=128)


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['phone', 'password']


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        exclude = ['last_login', 'is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions']
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is write-only
        }

    def create(self, validated_data):
        password = validated_data.pop('password')  # Extract the password
        user = UserAccount(**validated_data)  # Create the user instance
        user.set_password(password)  # Encrypt the password
        user.save()  # Save the user instance
        return user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.username
        token['email'] = user.email
        token['phone'] = user.phone
        token['user_type'] = user.user_type_id
        token['is_active'] = user.is_active
        token['is_staff'] = user.is_staff
        token['is_superuser'] = user.is_superuser

        return token
