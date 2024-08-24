from django.contrib.auth import authenticate, logout
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from Account.serializers import *
from Account.models import BlacklistedAccessTokens


# Create your views here.


@api_view(['POST'])
def user_login(request):
    try:
        data = JSONParser().parse(request)
        serializer = UserLogInSerializer(data=data)
        if serializer.is_valid():
            phone = serializer.validated_data.get('phone')
            password = serializer.validated_data.get('password')
            user = authenticate(phone=phone, password=password)

            if user is not None:
                refresh = MyTokenObtainPairSerializer.get_token(user)

                return Response({
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token)
                }, status=status.HTTP_200_OK)
            else:
                return Response("Invalid Credentials", status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response("Data Not Found \n" + str(e))


@api_view(['POST'])
def user_logout(request):
    try:
        if request.method == 'POST':
            refresh_token = request.query_params.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()

            access_token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
            blacklist_access_token = BlacklistedAccessTokens(access_token=access_token)
            blacklist_access_token.save()

            logout(request)

            return Response("User Logged Out", status=status.HTTP_200_OK)
    except Exception as e:
        return Response("Data Not Found \n" + str(e))


