from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
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

    @swagger_auto_schema(
        operation_description="Get all countries or a single country by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,  # This makes `pk` a query parameter
                description="Optional primary key for the country",
                type=openapi.TYPE_INTEGER,
                required=False  # Mark as optional
            )
        ],
        responses={200: openapi.Response('')}
    )
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

    @swagger_auto_schema(
        operation_description="Add new Country",
        request_body=CountrySerializer,
        responses={201: openapi.Response('')}
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

    @swagger_auto_schema(
        operation_description="Update an existing Country",
        request_body=CountrySerializer,
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,  # This makes `pk` a query parameter
                description="Primary key of the country to update",
                type=openapi.TYPE_INTEGER,
                required=True  # Mark as required for update
            )
        ],
        responses={200: openapi.Response('')}
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

    @swagger_auto_schema(
        operation_description="Delete a country by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,  # This makes `pk` a query parameter
                description="Primary key of the country to delete",
                type=openapi.TYPE_INTEGER,
                required=True  # Mark as required for deletion
            )
        ],
        responses={200: openapi.Response('')}
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
    @swagger_auto_schema(
        operation_description="Get all divisions or a single division by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Optional primary key for the division",
                type=openapi.TYPE_INTEGER,
                required=False
            )
        ],
        responses={200: openapi.Response('')}
    )
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

    @swagger_auto_schema(
        operation_description="Add new Division",
        request_body=DivisionSerializer,
        responses={201: openapi.Response('')}
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

    @swagger_auto_schema(
        operation_description="Update a Division",
        request_body=DivisionSerializer,
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the division to update",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={201: openapi.Response('')}
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

    @swagger_auto_schema(
        operation_description="Delete a division by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the division to delete",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={200: openapi.Response('')}
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
    @swagger_auto_schema(
        operation_description="Get all districts or a single district by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Optional primary key for the district",
                type=openapi.TYPE_INTEGER,
                required=False
            )
        ],
        responses={200: openapi.Response('')}
    )
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

    @swagger_auto_schema(
        operation_description="Add new District",
        request_body=DistrictSerializer,
        responses={201: openapi.Response('')}
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

    @swagger_auto_schema(
        operation_description="Update a District",
        request_body=DistrictSerializer,
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the district to update",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={201: openapi.Response('')}
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

    @swagger_auto_schema(
        operation_description="Delete a district by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the district to delete",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={200: openapi.Response('')}
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
    @swagger_auto_schema(
        operation_description="Get all upazilas or a single upazila by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Optional primary key for the upazila",
                type=openapi.TYPE_INTEGER,
                required=False
            )
        ],
        responses={200: openapi.Response('')}
    )
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

    @swagger_auto_schema(
        operation_description="Add new Upazila",
        request_body=UpazilaSerializer,
        responses={201: openapi.Response('')}
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

    @swagger_auto_schema(
        operation_description="Update an Upazila",
        request_body=UpazilaSerializer,
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the upazila to update",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={201: openapi.Response('')}
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

    @swagger_auto_schema(
        operation_description="Delete an upazila by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the upazila to delete",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={200: openapi.Response('')}
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
    @swagger_auto_schema(
        operation_description="Get all unions or a single union by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Optional primary key for the union",
                type=openapi.TYPE_INTEGER,
                required=False
            )
        ],
        responses={200: openapi.Response('')}
    )
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

    @swagger_auto_schema(
        operation_description="Add new Union",
        request_body=UnionSerializer,
        responses={201: openapi.Response('')}
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

    @swagger_auto_schema(
        operation_description="Update a Union",
        request_body=UnionSerializer,
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the union to update",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={201: openapi.Response('')}
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

    @swagger_auto_schema(
        operation_description="Delete a union by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the union to delete",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={200: openapi.Response('')}
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
    @swagger_auto_schema(
        operation_description="Get all wards or a single ward by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Optional primary key for the ward",
                type=openapi.TYPE_INTEGER,
                required=False
            )
        ],
        responses={200: openapi.Response('')}
    )
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

    @swagger_auto_schema(
        operation_description="Add new Ward",
        request_body=WardSerializer,
        responses={201: openapi.Response('')}
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

    @swagger_auto_schema(
        operation_description="Update a Ward",
        request_body=WardSerializer,
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the ward to update",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={201: openapi.Response('')}
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

    @swagger_auto_schema(
        operation_description="Delete a ward by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the ward to delete",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={200: openapi.Response('')}
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
    @swagger_auto_schema(
        operation_description="Get all city corporations or a single city corporation by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Optional primary key for the city corporation",
                type=openapi.TYPE_INTEGER,
                required=False
            )
        ],
        responses={200: openapi.Response('')}
    )
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

    @swagger_auto_schema(
        operation_description="Add new City Corporation",
        request_body=CityCorporationSerializer,
        responses={201: openapi.Response('')}
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

    @swagger_auto_schema(
        operation_description="Update a City Corporation",
        request_body=CityCorporationSerializer,
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the city corporation to update",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={201: openapi.Response('')}
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

    @swagger_auto_schema(
        operation_description="Delete a city corporation by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the city corporation to delete",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={200: openapi.Response('')}
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
    @swagger_auto_schema(
        operation_description="Get all municipalities or a single municipality by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Optional primary key for the municipality",
                type=openapi.TYPE_INTEGER,
                required=False
            )
        ],
        responses={200: openapi.Response('')}
    )
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

    @swagger_auto_schema(
        operation_description="Add new Municipality",
        request_body=MunicipalitySerializer,
        responses={201: openapi.Response('')}
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

    @swagger_auto_schema(
        operation_description="Update a Municipality",
        request_body=MunicipalitySerializer,
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the municipality to update",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={201: openapi.Response('')}
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

    @swagger_auto_schema(
        operation_description="Delete a municipality by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the municipality to delete",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={200: openapi.Response('')}
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
    @swagger_auto_schema(
        operation_description="Get all addresses or a single address by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Optional primary key for the address",
                type=openapi.TYPE_INTEGER,
                required=False
            )
        ],
        responses={200: openapi.Response('')}
    )

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

    @swagger_auto_schema(
        operation_description="Add new Address",
        request_body=AddressSerializer,
        responses={201: openapi.Response('')}
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

    @swagger_auto_schema(
        operation_description="Update an Address",
        request_body=AddressSerializer,
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the address to update",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={201: openapi.Response('')}
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

    @swagger_auto_schema(
        operation_description="Delete an address by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the address to delete",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={200: openapi.Response('')}
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
