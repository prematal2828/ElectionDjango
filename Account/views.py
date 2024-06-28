from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import UserType
from Account.serializers import *


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
                    'token': str(refresh),
                    'access': str(refresh.access_token)
                }, status=status.HTTP_200_OK)
            else:
                return Response("Invalid Credentials", status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response("Data Not Found \n" + str(e))


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def usertype_list(request):
    try:
        pk = request.query_params.get('pk')
        if pk == None:
            if request.method == 'GET':
                usertypes = UserType.objects.all()
                serializer = UserTypeSerializer(usertypes, many=True)
                return Response(serializer.data)
            if request.method == 'POST':
                data = JSONParser().parse(request)
                serializer = UserTypeSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response("User Type Added Successfully")
        else:
            usertype = UserType.objects.get(pk=pk)
            if request.method == 'GET':
                serializer = UserTypeSerializer(usertype, many=False)
                return Response(serializer.data)
            elif request.method == 'PUT':
                serializer = UserTypeSerializer(usertype, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response("User Type Updated Successfully")
            elif request.method == 'DELETE':
                usertype.delete()
                return Response("User Type Deleted Successfully")


    except Exception as e:
        return Response("Data Not Found \n" + str(e))
        # return JsonResponse(e)
