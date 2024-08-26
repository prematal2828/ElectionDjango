from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import *
from .models import *
from Account.models import checkBlacklistedAccessTokens


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def country_list(request):
    try:
        if not checkBlacklistedAccessTokens(request):
            pk = request.query_params.get('pk')
            if pk is None:
                if request.method == 'GET':
                    country_list = Country.objects.all()
                    serializer = CountrySerializer(country_list, many=True)
                    result_set = {
                        "msg": 'Returned Country list',
                        "data": serializer.data,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)

                if request.method == 'POST':
                    data = JSONParser().parse(request)
                    serializer = CountrySerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({"msg": "Country Added Successfully"}, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                country = Country.objects.get(pk=pk)
                if request.method == 'GET':
                    serializer = CountrySerializer(country, many=False)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                elif request.method == 'PUT':
                    serializer = CountrySerializer(country, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        result_set = {
                            "msg": 'Updated Country',
                            "data": serializer.data,
                        }
                        return Response(result_set, status=status.HTTP_200_OK)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                elif request.method == 'DELETE':
                    country.delete()
                    result_set = {
                        "msg": 'Deleted Country',
                        "data": None,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)
        else:
            result_set = {
                "msg": 'User Logged Out',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        result_set = {
            "msg": str(e),
            "data": None,
        }
        return Response(result_set, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes((JWTAuthentication,))
@permission_classes((IsAuthenticated,))
def division_list(request):
    try:
        if checkBlacklistedAccessTokens(request) is False:
            pk = request.query_params.get('pk')
            if pk == None:
                if request.method == 'GET':
                    division_list = Division.objects.all()
                    serializer = DivisionSerializer(division_list, many=True)

                    result_set = {
                        "msg": 'Returned Division list',
                        "data": serializer.data,
                    }

                    return Response(result_set, status=status.HTTP_200_OK)
                if request.method == 'POST':
                    data = JSONParser().parse(request)
                    serializer = DivisionSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response("Divisoion Added Successfully")
            else:
                division = Division.objects.get(pk=pk)
                if request.method == 'GET':
                    serializer = DivisionSerializer(division, many=False)
                    return Response(serializer.data)
                elif request.method == 'PUT':
                    serializer = DivisionSerializer(division, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        result_set = {
                            "msg": 'Updated Division',
                            "data": serializer.data,
                        }

                        return Response(result_set, status=status.HTTP_200_OK)
                elif request.method == 'DELETE':
                    division.delete()
                    result_set = {
                        "msg": 'Deleted Division',
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
