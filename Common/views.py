from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import *
from .models import *
from Account.models import checkBlacklistedAccessTokens


class CountryView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            pk = request.query_params.get('pk')
            if pk is None:  # List all countries
                countries = Country.objects.all()
                serializer = CountrySerializer(countries, many=True)
                result_set = {
                    "msg": 'Returned Country list',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            else:  # Retrieve a specific country by pk
                country = get_object_or_404(Country, pk=pk)
                serializer = CountrySerializer(country)
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request, *args, **kwargs):
        try:
            data = JSONParser().parse(request)
            serializer = CountrySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Country Added Successfully"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, *args, **kwargs):
        try:
            pk = request.query_params.get('pk')
            if pk is None:
                return Response({"msg": "pk is required for updating"}, status=status.HTTP_400_BAD_REQUEST)

            country = get_object_or_404(Country, pk=pk)
            serializer = CountrySerializer(country, data=request.data)
            if serializer.is_valid():
                serializer.save()
                result_set = {
                    "msg": 'Updated Country',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, *args, **kwargs):
        try:
            pk = request.query_params.get('pk')
            if pk is None:
                return Response({"msg": "pk is required for deletion"}, status=status.HTTP_400_BAD_REQUEST)

            country = get_object_or_404(Country, pk=pk)
            country.delete()
            result_set = {
                "msg": 'Deleted Country',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )


class DivisionView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            pk = request.query_params.get('pk')

            if pk is None:  # List all divisions
                divisions = Division.objects.all()
                serializer = DivisionSerializer(divisions, many=True, include_country=True)
                result_set = {
                    "msg": 'Returned Division list',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            else:  # Retrieve a specific division by pk
                division = get_object_or_404(Division, pk=pk)
                serializer = DivisionSerializer(division)
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request, *args, **kwargs):
        try:
            data = JSONParser().parse(request)
            serializer = DivisionSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Division Added Successfully"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, *args, **kwargs):
        try:
            pk = request.query_params.get('pk')
            if pk is None:
                return Response({"msg": "pk is required for updating"}, status=status.HTTP_400_BAD_REQUEST)

            division = get_object_or_404(Division, pk=pk)
            serializer = DivisionSerializer(division, data=request.data)
            if serializer.is_valid():
                serializer.save()
                result_set = {
                    "msg": 'Updated Division',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, *args, **kwargs):
        try:
            pk = request.query_params.get('pk')
            if pk is None:
                return Response({"msg": "pk is required for deletion"}, status=status.HTTP_400_BAD_REQUEST)

            division = get_object_or_404(Division, pk=pk)
            division.delete()
            result_set = {
                "msg": 'Deleted Division',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_200_OK)


        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )


class DistrictView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            pk = request.query_params.get('pk')
            if pk is None:
                district_list = District.objects.all()
                serializer = DistrictSerializer(district_list, many=True)
                result_set = {
                    "msg": 'Returned District list',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            else:
                district = District.objects.get(pk=pk)
                serializer = DistrictSerializer(district, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request, *args, **kwargs):
        try:
            data = JSONParser().parse(request)
            serializer = DistrictSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "District Added Successfully"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, *args, **kwargs):
        try:
            pk = request.query_params.get('pk')
            district = District.objects.get(pk)
            serializer = DistrictSerializer(district, data=request.data)
            if serializer.is_valid():
                serializer.save()
                result_set = {
                    "msg": 'Updated District',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, *args, **kwargs):
        try:
            pk = request.query_params.get('pk')
            district = District.objects.get(pk)
            district.delete()
            result_set = {
                "msg": 'Deleted District',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )


class UpazilaView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # Check if a specific primary key (pk) is provided
            pk = request.query_params.get('pk')

            if pk is None:  # List all Upazilas
                upazilas = Upazila.objects.all()
                serializer = UpazilaSerializer(upazilas, many=True)
                result_set = {
                    "msg": 'Returned Upazila list',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            else:  # Retrieve a specific Upazila by pk
                upazila = get_object_or_404(Upazila, pk=pk)
                serializer = UpazilaSerializer(upazila)
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request, *args, **kwargs):
        try:
            # Parse the incoming request data
            data = JSONParser().parse(request)
            serializer = UpazilaSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"msg": "Upazila Added Successfully"},
                    status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, *args, **kwargs):
        try:
            # Retrieve the Upazila object by primary key
            pk = request.query_params.get('pk')
            if pk is None:
                return Response(
                    {"msg": "pk is required for updating"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            upazila = get_object_or_404(Upazila, pk=pk)
            serializer = UpazilaSerializer(upazila, data=request.data)

            if serializer.is_valid():
                serializer.save()
                result_set = {
                    "msg": 'Updated Upazila',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, *args, **kwargs):
        try:
            # Retrieve the Upazila object by primary key
            pk = request.query_params.get('pk')
            if pk is None:
                return Response(
                    {"msg": "pk is required for deletion"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            upazila = get_object_or_404(Upazila, pk=pk)
            upazila.delete()

            result_set = {
                "msg": 'Deleted Upazila',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )


class UpazilaView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # Check if a specific primary key (pk) is provided
            pk = request.query_params.get('pk')

            if pk is None:  # List all Upazilas
                upazilas = Upazila.objects.all()
                serializer = UpazilaSerializer(upazilas, many=True)
                result_set = {
                    "msg": 'Returned Upazila list',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            else:  # Retrieve a specific Upazila by pk
                upazila = get_object_or_404(Upazila, pk=pk)
                serializer = UpazilaSerializer(upazila)
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request, *args, **kwargs):
        try:
            # Parse the incoming request data
            data = JSONParser().parse(request)
            serializer = UpazilaSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"msg": "Upazila Added Successfully"},
                    status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, *args, **kwargs):
        try:
            # Retrieve the Upazila object by primary key
            pk = request.query_params.get('pk')
            if pk is None:
                return Response(
                    {"msg": "pk is required for updating"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            upazila = get_object_or_404(Upazila, pk=pk)
            serializer = UpazilaSerializer(upazila, data=request.data)

            if serializer.is_valid():
                serializer.save()
                result_set = {
                    "msg": 'Updated Upazila',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, *args, **kwargs):
        try:
            # Retrieve the Upazila object by primary key
            pk = request.query_params.get('pk')
            if pk is None:
                return Response(
                    {"msg": "pk is required for deletion"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            upazila = get_object_or_404(Upazila, pk=pk)
            upazila.delete()

            result_set = {
                "msg": 'Deleted Upazila',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )


class UnionView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            primary_key = request.query_params.get('pk')

            if primary_key is None:  # List all Unions
                unions = Union.objects.all()
                serializer = UnionSerializer(unions, many=True)
                result_set = {
                    "msg": 'Returned Union list',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            else:  # Retrieve a specific Union by primary key
                union = get_object_or_404(Union, pk=primary_key)
                serializer = UnionSerializer(union)
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request, *args, **kwargs):
        try:
            data = JSONParser().parse(request)
            serializer = UnionSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"msg": "Union Added Successfully"},
                    status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, *args, **kwargs):
        try:
            primary_key = request.query_params.get('pk')
            if primary_key is None:
                return Response(
                    {"msg": "Primary key (pk) is required for updating"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            union = get_object_or_404(Union, pk=primary_key)
            serializer = UnionSerializer(union, data=request.data)
            if serializer.is_valid():
                serializer.save()
                result_set = {
                    "msg": 'Updated Union',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, *args, **kwargs):
        try:
            primary_key = request.query_params.get('pk')
            if primary_key is None:
                return Response(
                    {"msg": "Primary key (pk) is required for deletion"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            union = get_object_or_404(Union, pk=primary_key)
            union.delete()

            result_set = {
                "msg": 'Deleted Union',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )


class WardView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            primary_key = request.query_params.get('pk')

            if primary_key is None:  # List all Wards
                wards = Ward.objects.all()
                serializer = WardSerializer(wards, many=True)
                result_set = {
                    "msg": 'Returned Ward list',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            else:  # Retrieve a specific Ward by primary key
                ward = get_object_or_404(Ward, pk=primary_key)
                serializer = WardSerializer(ward)
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request, *args, **kwargs):
        try:
            data = JSONParser().parse(request)
            serializer = WardSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"msg": "Ward Added Successfully"},
                    status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, *args, **kwargs):
        try:
            primary_key = request.query_params.get('pk')
            if primary_key is None:
                return Response(
                    {"msg": "Primary key (pk) is required for updating"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            ward = get_object_or_404(Ward, pk=primary_key)
            serializer = WardSerializer(ward, data=request.data)
            if serializer.is_valid():
                serializer.save()
                result_set = {
                    "msg": 'Updated Ward',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, *args, **kwargs):
        try:
            primary_key = request.query_params.get('pk')
            if primary_key is None:
                return Response(
                    {"msg": "Primary key (pk) is required for deletion"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            ward = get_object_or_404(Ward, pk=primary_key)
            ward.delete()

            result_set = {
                "msg": 'Deleted Ward',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )


class CityCorporationView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            primary_key = request.query_params.get('pk')

            if primary_key is None:  # List all CityCorporations
                city_corporations = CityCorporation.objects.all()
                serializer = CityCorporationSerializer(city_corporations, many=True)
                result_set = {
                    "msg": 'Returned CityCorporation list',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            else:  # Retrieve a specific CityCorporation by primary key
                city_corporation = get_object_or_404(CityCorporation, pk=primary_key)
                serializer = CityCorporationSerializer(city_corporation)
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request, *args, **kwargs):
        try:
            data = JSONParser().parse(request)
            serializer = CityCorporationSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"msg": "CityCorporation Added Successfully"},
                    status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, *args, **kwargs):
        try:
            primary_key = request.query_params.get('pk')
            if primary_key is None:
                return Response(
                    {"msg": "Primary key (pk) is required for updating"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            city_corporation = get_object_or_404(CityCorporation, pk=primary_key)
            serializer = CityCorporationSerializer(city_corporation, data=request.data)
            if serializer.is_valid():
                serializer.save()
                result_set = {
                    "msg": 'Updated CityCorporation',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, *args, **kwargs):
        try:
            primary_key = request.query_params.get('pk')
            if primary_key is None:
                return Response(
                    {"msg": "Primary key (pk) is required for deletion"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            city_corporation = get_object_or_404(CityCorporation, pk=primary_key)
            city_corporation.delete()

            result_set = {
                "msg": 'Deleted CityCorporation',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )


class MunicipalityView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            primary_key = request.query_params.get('pk')

            if primary_key is None:  # List all Municipalities
                municipalities = Municipality.objects.all()
                serializer = MunicipalitySerializer(municipalities, many=True)
                result_set = {
                    "msg": 'Returned Municipality list',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            else:  # Retrieve a specific Municipality by primary key
                municipality = get_object_or_404(Municipality, pk=primary_key)
                serializer = MunicipalitySerializer(municipality)
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request, *args, **kwargs):
        try:
            data = JSONParser().parse(request)
            serializer = MunicipalitySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"msg": "Municipality Added Successfully"},
                    status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, *args, **kwargs):
        try:
            primary_key = request.query_params.get('pk')
            if primary_key is None:
                return Response(
                    {"msg": "Primary key (pk) is required for updating"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            municipality = get_object_or_404(Municipality, pk=primary_key)
            serializer = MunicipalitySerializer(municipality, data=request.data)
            if serializer.is_valid():
                serializer.save()
                result_set = {
                    "msg": 'Updated Municipality',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, *args, **kwargs):
        try:
            primary_key = request.query_params.get('pk')
            if primary_key is None:
                return Response(
                    {"msg": "Primary key (pk) is required for deletion"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            municipality = get_object_or_404(Municipality, pk=primary_key)
            municipality.delete()

            result_set = {
                "msg": 'Deleted Municipality',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )


class AddressView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            primary_key = request.query_params.get('pk')

            if primary_key is None:  # List all Addresses
                addresses = Address.objects.all()
                serializer = AddressSerializer(addresses, many=True)
                result_set = {
                    "msg": 'Returned Address list',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            else:  # Retrieve a specific Address by primary key
                address = get_object_or_404(Address, pk=primary_key)
                serializer = AddressSerializer(address)
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request, *args, **kwargs):
        try:
            data = JSONParser().parse(request)
            serializer = AddressSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"msg": "Address Added Successfully"},
                    status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, *args, **kwargs):
        try:
            primary_key = request.query_params.get('pk')
            if primary_key is None:
                return Response(
                    {"msg": "Primary key (pk) is required for updating"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            address = get_object_or_404(Address, pk=primary_key)
            serializer = AddressSerializer(address, data=request.data)
            if serializer.is_valid():
                serializer.save()
                result_set = {
                    "msg": 'Updated Address',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, *args, **kwargs):
        try:
            primary_key = request.query_params.get('pk')
            if primary_key is None:
                return Response(
                    {"msg": "Primary key (pk) is required for deletion"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            address = get_object_or_404(Address, pk=primary_key)
            address.delete()

            result_set = {
                "msg": 'Deleted Address',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )
