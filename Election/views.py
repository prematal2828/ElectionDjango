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
def election_type_list(request):
    try:
        if not checkBlacklistedAccessTokens(request):
            primary_key = request.query_params.get('pk')
            if primary_key is None:
                if request.method == 'GET':
                    election_type_list = ElectionType.objects.all()
                    serializer = ElectionTypeSerializer(election_type_list, many=True)
                    result_set = {
                        "msg": 'Returned ElectionType list',
                        "data": serializer.data,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)

                if request.method == 'POST':
                    data = JSONParser().parse(request)
                    serializer = ElectionTypeSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({"msg": "ElectionType Added Successfully"}, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                election_type = ElectionType.objects.get(pk=primary_key)
                if request.method == 'GET':
                    serializer = ElectionTypeSerializer(election_type, many=False)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                elif request.method == 'PUT':
                    serializer = ElectionTypeSerializer(election_type, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        result_set = {
                            "msg": 'Updated ElectionType',
                            "data": serializer.data,
                        }
                        return Response(result_set, status=status.HTTP_200_OK)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                elif request.method == 'DELETE':
                    election_type.delete()
                    result_set = {
                        "msg": 'Deleted ElectionType',
                        "data": None,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)
        else:
            result_set = {
                "msg": 'User Logged Out',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_401_UNAUTHORIZED)

    except ElectionType.DoesNotExist:
        result_set = {
            "msg": "ElectionType not found",
            "data": None,
        }
        return Response(result_set, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        result_set = {
            "msg": str(e),
            "data": None,
        }
        return Response(result_set, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def election_info_list(request):
    try:
        if not checkBlacklistedAccessTokens(request):
            primary_key = request.query_params.get('pk')
            if primary_key is None:
                if request.method == 'GET':
                    election_info_list = ElectionInfo.objects.all()
                    serializer = ElectionInfoSerializer(election_info_list, many=True)
                    result_set = {
                        "msg": 'Returned ElectionInfo list',
                        "data": serializer.data,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)

                if request.method == 'POST':
                    data = JSONParser().parse(request)
                    serializer = ElectionInfoSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({"msg": "ElectionInfo Added Successfully"}, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                election_info = ElectionInfo.objects.get(pk=primary_key)
                if request.method == 'GET':
                    serializer = ElectionInfoSerializer(election_info, many=False)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                elif request.method == 'PUT':
                    serializer = ElectionInfoSerializer(election_info, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        result_set = {
                            "msg": 'Updated ElectionInfo',
                            "data": serializer.data,
                        }
                        return Response(result_set, status=status.HTTP_200_OK)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                elif request.method == 'DELETE':
                    election_info.delete()
                    result_set = {
                        "msg": 'Deleted ElectionInfo',
                        "data": None,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)
        else:
            result_set = {
                "msg": 'User Logged Out',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_401_UNAUTHORIZED)

    except ElectionInfo.DoesNotExist:
        result_set = {
            "msg": "ElectionInfo not found",
            "data": None,
        }
        return Response(result_set, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        result_set = {
            "msg": str(e),
            "data": None,
        }
        return Response(result_set, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def election_data_list(request):
    try:
        if not checkBlacklistedAccessTokens(request):
            primary_key = request.query_params.get('pk')
            if primary_key is None:
                if request.method == 'GET':
                    election_data_list = ElectionData.objects.all()
                    serializer = ElectionDataSerializer(election_data_list, many=True)
                    result_set = {
                        "msg": 'Returned ElectionData list',
                        "data": serializer.data,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)

                if request.method == 'POST':
                    data = JSONParser().parse(request)
                    serializer = ElectionDataSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({"msg": "ElectionData Added Successfully"}, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                election_data = ElectionData.objects.get(pk=primary_key)
                if request.method == 'GET':
                    serializer = ElectionDataSerializer(election_data, many=False)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                elif request.method == 'PUT':
                    serializer = ElectionDataSerializer(election_data, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        result_set = {
                            "msg": 'Updated ElectionData',
                            "data": serializer.data,
                        }
                        return Response(result_set, status=status.HTTP_200_OK)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                elif request.method == 'DELETE':
                    election_data.delete()
                    result_set = {
                        "msg": 'Deleted ElectionData',
                        "data": None,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)
        else:
            result_set = {
                "msg": 'User Logged Out',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_401_UNAUTHORIZED)

    except ElectionData.DoesNotExist:
        result_set = {
            "msg": "ElectionData not found",
            "data": None,
        }
        return Response(result_set, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        result_set = {
            "msg": str(e),
            "data": None,
        }
        return Response(result_set, status=status.HTTP_400_BAD_REQUEST)
