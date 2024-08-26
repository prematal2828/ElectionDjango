from django.contrib.auth import authenticate, logout
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
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


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes((JWTAuthentication,))
@permission_classes((IsAuthenticated,))
def usertype_list(request):
    try:
        if checkBlacklistedAccessTokens(request) is False:
            pk = request.query_params.get('pk')
            if pk == None:
                if request.method == 'GET':
                    user_types = UserType.objects.all()
                    serializer = UserTypeSerializer(user_types, many=True)

                    result_set = {
                        "msg": 'Returned User Types list',
                        "data": serializer.data,
                    }

                    return Response(result_set, status=status.HTTP_200_OK)
                if request.method == 'POST':
                    data = JSONParser().parse(request)
                    serializer = UserTypeSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response("User Type Added Successfully")
            else:
                user_type = UserType.objects.get(pk=pk)
                if request.method == 'GET':
                    serializer = UserTypeSerializer(user_type, many=False)
                    return Response(serializer.data)
                elif request.method == 'PUT':
                    serializer = UserTypeSerializer(user_type, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        result_set = {
                            "msg": 'Updated User Type',
                            "data": serializer.data,
                        }

                        return Response(result_set, status=status.HTTP_200_OK)
                elif request.method == 'DELETE':
                    user_type.delete()
                    result_set = {
                        "msg": 'Deleted User Type',
                        "data": None,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)

        else:
            result_set = {
                "msg": 'User Logged Out',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_200_OK)

    except Exception as e:
        result_set = {
            "msg": e,
            "data": None,
        }
        return Response(result_set, status=status.HTTP_400_BAD_REQUEST)
