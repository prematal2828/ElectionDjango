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
        fields = '__all__'


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
