from django.contrib.auth import authenticate, logout, login
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from Account.serializers import *
from Account.models import BlacklistedAccessTokens

from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate


# Create your views here.


class UserLoginView(APIView):

    @swagger_auto_schema(
        operation_description="Login to your account",
        request_body=UserLogInSerializer,
        responses={200: openapi.Response('')}
    )
    def post(self, request, *args, **kwargs):
        try:
            data = request.data  # `request.data` automatically handles parsing in CBVs
            serializer = UserLogInSerializer(data=data)

            if serializer.is_valid():
                phone = serializer.validated_data.get('phone')
                password = serializer.validated_data.get('password')
                user = authenticate(phone=phone, password=password)

                if user is not None:
                    login(request, user)
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
            return Response("Data Not Found \n" + str(e), status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Get the refresh token from query parameters
            refresh_token = request.query_params.get('refresh_token')
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()  # Blacklist the refresh token

            # Get the access token from request headers and blacklist it
            auth_header = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')
            if len(auth_header) == 2:
                access_token = auth_header[1]
                if checkBlacklistedAccessTokens(request):
                    blacklist_access_token = BlacklistedAccessTokens(access_token=access_token)
                    blacklist_access_token.save()

            # Log out the user
            logout(request)

            return Response("User Logged Out", status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"msg": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)


class UserTypeView(APIView):
    @swagger_auto_schema(
        operation_description="Get all user types or single user type by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,  # This makes `pk` a query parameter
                description="Optional primary key for the user type",
                type=openapi.TYPE_INTEGER,
                required=False  # Mark as optional
            )
        ],
        responses={200: openapi.Response('')}
    )
    def get(self, request, *args, **kwargs):
        try:
            pk = request.query_params.get('pk')
            if pk is None:  # List all user types
                user_types = UserType.objects.all()
                serializer = UserTypeSerializer(user_types, many=True)
                result_set = {
                    "msg": 'User Types list is empty' if serializer.data is None else 'Returned User Types list',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            else:  # Retrieve a single user type by pk
                user_type = get_object_or_404(UserType, pk=pk)
                serializer = UserTypeSerializer(user_type)
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"msg": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Add new user type",
        request_body=UserTypeSerializer,
        responses={201: openapi.Response('')}
    )
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = UserTypeSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response("User Type Added Successfully", status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"msg": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Update user type",
        request_body=UserTypeSerializer,
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,  # This makes `pk` a query parameter
                description="Id of the user type",
                type=openapi.TYPE_INTEGER,
                required=True  # Mark as optional
            )
        ],
        responses={201: openapi.Response('')}
    )
    def put(self, request, *args, **kwargs):

        try:
            pk = request.query_params.get('pk')
            if pk is None:
                return Response({"msg": "pk is required for updating"}, status=status.HTTP_400_BAD_REQUEST)

            user_type = get_object_or_404(UserType, pk=pk)
            serializer = UserTypeSerializer(user_type, data=request.data)
            if serializer.is_valid():
                serializer.save()
                result_set = {
                    "msg": 'Updated User Type',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"msg": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Update user type",
        request_body=UserTypeSerializer,
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,  # This makes `pk` a query parameter
                description="Id of the user type",
                type=openapi.TYPE_INTEGER,
                required=True  # Mark as optional
            )
        ],
        responses={200: openapi.Response('')}
    )
    def delete(self, request, *args, **kwargs):

        try:
            pk = request.query_params.get('pk')
            if pk is None:
                return Response({"msg": "pk is required for deletion"}, status=status.HTTP_400_BAD_REQUEST)

            user_type = get_object_or_404(UserType, pk=pk)
            user_type.delete()
            result_set = {
                "msg": 'Deleted User Type',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"msg": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    @swagger_auto_schema(
        operation_description="Get all user or single user by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,  # This makes `pk` a query parameter
                description="Optional primary key for the user",
                type=openapi.TYPE_INTEGER,
                required=False  # Mark as optional
            )
        ],
        responses={200: openapi.Response('')}
    )
    def get(self, request, *args, **kwargs):

        try:
            pk = request.query_params.get('pk')

            if pk is None:  # List all users
                users = UserAccount.objects.all()
                serializer = UserAccountSerializer(users, many=True)
                result_set = {
                    "msg": 'Users list is empty' if serializer.data is None else 'Returned Users list',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            else:  # Retrieve a single user by pk
                user = get_object_or_404(UserAccount, pk=pk)
                serializer = UserAccountSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"msg": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Add new user",
        request_body=UserAccountSerializer,
        responses={201: openapi.Response('')}
    )
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = UserAccountSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response("User Added Successfully", status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"msg": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Update user",
        request_body=UserAccountSerializer,
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,  # This makes `pk` a query parameter
                description="Optional primary key for the user type",
                type=openapi.TYPE_INTEGER,
                required=False  # Mark as optional
            )
        ],
        responses={201: openapi.Response('')}
    )
    def put(self, request, pk, *args, **kwargs):
        try:
            user = get_object_or_404(UserAccount, pk=pk)
            serializer = UserAccountSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                result_set = {
                    "msg": 'Updated User',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"msg": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        try:
            user = get_object_or_404(UserAccount, pk=pk)
            user.delete()
            result_set = {
                "msg": 'Deleted User',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"msg": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)
