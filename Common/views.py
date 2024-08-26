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


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def district_list(request):
    try:
        if not checkBlacklistedAccessTokens(request):
            primary_key = request.query_params.get('pk')
            if primary_key is None:
                if request.method == 'GET':
                    district_list = District.objects.all()
                    serializer = DistrictSerializer(district_list, many=True)
                    result_set = {
                        "msg": 'Returned District list',
                        "data": serializer.data,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)

                if request.method == 'POST':
                    data = JSONParser().parse(request)
                    serializer = DistrictSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({"msg": "District Added Successfully"}, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                district = District.objects.get(pk=primary_key)
                if request.method == 'GET':
                    serializer = DistrictSerializer(district, many=False)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                elif request.method == 'PUT':
                    serializer = DistrictSerializer(district, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        result_set = {
                            "msg": 'Updated District',
                            "data": serializer.data,
                        }
                        return Response(result_set, status=status.HTTP_200_OK)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                elif request.method == 'DELETE':
                    district.delete()
                    result_set = {
                        "msg": 'Deleted District',
                        "data": None,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)
        else:
            result_set = {
                "msg": 'User Logged Out',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_401_UNAUTHORIZED)

    except District.DoesNotExist:
        result_set = {
            "msg": "District not found",
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
def upazila_list(request):
    try:
        if not checkBlacklistedAccessTokens(request):
            primary_key = request.query_params.get('pk')
            if primary_key is None:
                if request.method == 'GET':
                    upazila_list = Upazila.objects.all()
                    serializer = UpazilaSerializer(upazila_list, many=True)
                    result_set = {
                        "msg": 'Returned Upazila list',
                        "data": serializer.data,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)

                if request.method == 'POST':
                    data = JSONParser().parse(request)
                    serializer = UpazilaSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({"msg": "Upazila Added Successfully"}, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                upazila = Upazila.objects.get(pk=primary_key)
                if request.method == 'GET':
                    serializer = UpazilaSerializer(upazila, many=False)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                elif request.method == 'PUT':
                    serializer = UpazilaSerializer(upazila, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        result_set = {
                            "msg": 'Updated Upazila',
                            "data": serializer.data,
                        }
                        return Response(result_set, status=status.HTTP_200_OK)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                elif request.method == 'DELETE':
                    upazila.delete()
                    result_set = {
                        "msg": 'Deleted Upazila',
                        "data": None,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)
        else:
            result_set = {
                "msg": 'User Logged Out',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_401_UNAUTHORIZED)

    except Upazila.DoesNotExist:
        result_set = {
            "msg": "Upazila not found",
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
def upazila_list(request):
    try:
        if not checkBlacklistedAccessTokens(request):
            primary_key = request.query_params.get('pk')
            if primary_key is None:
                if request.method == 'GET':
                    upazila_list = Upazila.objects.all()
                    serializer = UpazilaSerializer(upazila_list, many=True)
                    result_set = {
                        "msg": 'Returned Upazila list',
                        "data": serializer.data,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)

                if request.method == 'POST':
                    data = JSONParser().parse(request)
                    serializer = UpazilaSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({"msg": "Upazila Added Successfully"}, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                upazila = Upazila.objects.get(pk=primary_key)
                if request.method == 'GET':
                    serializer = UpazilaSerializer(upazila, many=False)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                elif request.method == 'PUT':
                    serializer = UpazilaSerializer(upazila, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        result_set = {
                            "msg": 'Updated Upazila',
                            "data": serializer.data,
                        }
                        return Response(result_set, status=status.HTTP_200_OK)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                elif request.method == 'DELETE':
                    upazila.delete()
                    result_set = {
                        "msg": 'Deleted Upazila',
                        "data": None,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)
        else:
            result_set = {
                "msg": 'User Logged Out',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_401_UNAUTHORIZED)

    except Upazila.DoesNotExist:
        result_set = {
            "msg": "Upazila not found",
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
def union_list(request):
    try:
        if not checkBlacklistedAccessTokens(request):
            primary_key = request.query_params.get('pk')
            if primary_key is None:
                if request.method == 'GET':
                    union_list = Union.objects.all()
                    serializer = UnionSerializer(union_list, many=True)
                    result_set = {
                        "msg": 'Returned Union list',
                        "data": serializer.data,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)

                if request.method == 'POST':
                    data = JSONParser().parse(request)
                    serializer = UnionSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({"msg": "Union Added Successfully"}, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                union = Union.objects.get(pk=primary_key)
                if request.method == 'GET':
                    serializer = UnionSerializer(union, many=False)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                elif request.method == 'PUT':
                    serializer = UnionSerializer(union, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        result_set = {
                            "msg": 'Updated Union',
                            "data": serializer.data,
                        }
                        return Response(result_set, status=status.HTTP_200_OK)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                elif request.method == 'DELETE':
                    union.delete()
                    result_set = {
                        "msg": 'Deleted Union',
                        "data": None,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)
        else:
            result_set = {
                "msg": 'User Logged Out',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_401_UNAUTHORIZED)

    except Union.DoesNotExist:
        result_set = {
            "msg": "Union not found",
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
def ward_list(request):
    try:
        if not checkBlacklistedAccessTokens(request):
            primary_key = request.query_params.get('pk')
            if primary_key is None:
                if request.method == 'GET':
                    ward_list = Ward.objects.all()
                    serializer = WardSerializer(ward_list, many=True)
                    result_set = {
                        "msg": 'Returned Ward list',
                        "data": serializer.data,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)

                if request.method == 'POST':
                    data = JSONParser().parse(request)
                    serializer = WardSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({"msg": "Ward Added Successfully"}, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                ward = Ward.objects.get(pk=primary_key)
                if request.method == 'GET':
                    serializer = WardSerializer(ward, many=False)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                elif request.method == 'PUT':
                    serializer = WardSerializer(ward, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        result_set = {
                            "msg": 'Updated Ward',
                            "data": serializer.data,
                        }
                        return Response(result_set, status=status.HTTP_200_OK)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                elif request.method == 'DELETE':
                    ward.delete()
                    result_set = {
                        "msg": 'Deleted Ward',
                        "data": None,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)
        else:
            result_set = {
                "msg": 'User Logged Out',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_401_UNAUTHORIZED)

    except Ward.DoesNotExist:
        result_set = {
            "msg": "Ward not found",
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
def city_corporation_list(request):
    try:
        if not checkBlacklistedAccessTokens(request):
            primary_key = request.query_params.get('pk')
            if primary_key is None:
                if request.method == 'GET':
                    city_corporation_list = CityCorporation.objects.all()
                    serializer = CityCorporationSerializer(city_corporation_list, many=True)
                    result_set = {
                        "msg": 'Returned CityCorporation list',
                        "data": serializer.data,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)

                if request.method == 'POST':
                    data = JSONParser().parse(request)
                    serializer = CityCorporationSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({"msg": "CityCorporation Added Successfully"}, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                city_corporation = CityCorporation.objects.get(pk=primary_key)
                if request.method == 'GET':
                    serializer = CityCorporationSerializer(city_corporation, many=False)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                elif request.method == 'PUT':
                    serializer = CityCorporationSerializer(city_corporation, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        result_set = {
                            "msg": 'Updated CityCorporation',
                            "data": serializer.data,
                        }
                        return Response(result_set, status=status.HTTP_200_OK)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                elif request.method == 'DELETE':
                    city_corporation.delete()
                    result_set = {
                        "msg": 'Deleted CityCorporation',
                        "data": None,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)
        else:
            result_set = {
                "msg": 'User Logged Out',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_401_UNAUTHORIZED)

    except CityCorporation.DoesNotExist:
        result_set = {
            "msg": "CityCorporation not found",
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
def municipality_list(request):
    try:
        if not checkBlacklistedAccessTokens(request):
            primary_key = request.query_params.get('pk')
            if primary_key is None:
                if request.method == 'GET':
                    municipality_list = Municipality.objects.all()
                    serializer = MunicipalitySerializer(municipality_list, many=True)
                    result_set = {
                        "msg": 'Returned Municipality list',
                        "data": serializer.data,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)

                if request.method == 'POST':
                    data = JSONParser().parse(request)
                    serializer = MunicipalitySerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({"msg": "Municipality Added Successfully"}, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                municipality = Municipality.objects.get(pk=primary_key)
                if request.method == 'GET':
                    serializer = MunicipalitySerializer(municipality, many=False)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                elif request.method == 'PUT':
                    serializer = MunicipalitySerializer(municipality, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        result_set = {
                            "msg": 'Updated Municipality',
                            "data": serializer.data,
                        }
                        return Response(result_set, status=status.HTTP_200_OK)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                elif request.method == 'DELETE':
                    municipality.delete()
                    result_set = {
                        "msg": 'Deleted Municipality',
                        "data": None,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)
        else:
            result_set = {
                "msg": 'User Logged Out',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_401_UNAUTHORIZED)

    except Municipality.DoesNotExist:
        result_set = {
            "msg": "Municipality not found",
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
def address_list(request):
    try:
        if not checkBlacklistedAccessTokens(request):
            primary_key = request.query_params.get('pk')
            if primary_key is None:
                if request.method == 'GET':
                    address_list = Address.objects.all()
                    serializer = AddressSerializer(address_list, many=True)
                    result_set = {
                        "msg": 'Returned Address list',
                        "data": serializer.data,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)

                if request.method == 'POST':
                    data = JSONParser().parse(request)
                    serializer = AddressSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({"msg": "Address Added Successfully"}, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                address = Address.objects.get(pk=primary_key)
                if request.method == 'GET':
                    serializer = AddressSerializer(address, many=False)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                elif request.method == 'PUT':
                    serializer = AddressSerializer(address, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        result_set = {
                            "msg": 'Updated Address',
                            "data": serializer.data,
                        }
                        return Response(result_set, status=status.HTTP_200_OK)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                elif request.method == 'DELETE':
                    address.delete()
                    result_set = {
                        "msg": 'Deleted Address',
                        "data": None,
                    }
                    return Response(result_set, status=status.HTTP_200_OK)
        else:
            result_set = {
                "msg": 'User Logged Out',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_401_UNAUTHORIZED)

    except Address.DoesNotExist:
        result_set = {
            "msg": "Address not found",
            "data": None,
        }
        return Response(result_set, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        result_set = {
            "msg": str(e),
            "data": None,
        }
        return Response(result_set, status=status.HTTP_400_BAD_REQUEST)
