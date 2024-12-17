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


class ElectionTypeView(APIView):

    @swagger_auto_schema(
        operation_description="Get all election types or a single election type by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,  # `pk` as a query parameter
                description="Optional primary key for the election type",
                type=openapi.TYPE_INTEGER,
                required=False  # Mark as optional
            )
        ],
        responses={200: openapi.Response('')}
    )
    def get(self, request, *args, **kwargs):
        try:
            pk = request.query_params.get('pk')
            if pk is None:  # List all election types
                election_types = ElectionType.objects.all()
                serializer = ElectionTypeSerializer(election_types, many=True)
                result_set = {
                    "msg": 'ElectionType list is empty' if serializer.data is None else 'Returned ElectionType list',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            else:  # Retrieve a specific election type by pk
                election_type = get_object_or_404(ElectionType, pk=pk)
                serializer = ElectionTypeSerializer(election_type)
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    @swagger_auto_schema(
        operation_description="Add a new election type",
        request_body=ElectionTypeSerializer,
        responses={201: openapi.Response('')}
    )
    def post(self, request, *args, **kwargs):
        try:
            data = JSONParser().parse(request)
            serializer = ElectionTypeSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "ElectionType Added Successfully"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    @swagger_auto_schema(
        operation_description="Update an existing election type",
        request_body=ElectionTypeSerializer,
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,  # `pk` as a query parameter
                description="Primary key of the election type to update",
                type=openapi.TYPE_INTEGER,
                required=True  # Mark as required
            )
        ],
        responses={200: openapi.Response('')}
    )
    def put(self, request, *args, **kwargs):
        try:
            pk = request.query_params.get('pk')
            if pk is None:
                return Response({"msg": "pk is required for updating"}, status=status.HTTP_400_BAD_REQUEST)

            election_type = get_object_or_404(ElectionType, pk=pk)
            serializer = ElectionTypeSerializer(election_type, data=request.data)
            if serializer.is_valid():
                serializer.save()
                result_set = {
                    "msg": 'Updated ElectionType',
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
        operation_description="Delete an election type by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,  # `pk` as a query parameter
                description="Primary key of the election type to delete",
                type=openapi.TYPE_INTEGER,
                required=True  # Mark as required
            )
        ],
        responses={200: openapi.Response('')}
    )
    def delete(self, request, *args, **kwargs):
        try:
            pk = request.query_params.get('pk')
            if pk is None:
                return Response({"msg": "pk is required for deletion"}, status=status.HTTP_400_BAD_REQUEST)

            election_type = get_object_or_404(ElectionType, pk=pk)
            election_type.delete()
            result_set = {
                "msg": 'Deleted ElectionType',
                "data": None,
            }
            return Response(result_set, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )


class ElectionCenterView(APIView):

    @swagger_auto_schema(
        operation_description="Get all election centers or a single election center by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Optional primary key for the election center",
                type=openapi.TYPE_INTEGER,
                required=False
            )
        ],
        responses={200: openapi.Response('')}
    )
    def get(self, request, *args, **kwargs):
        try:
            pk = request.query_params.get('pk')
            if pk is None:  # List all election centers
                election_center_list = ElectionCenter.objects.all()
                serializer = ElectionCenterSerializer(election_center_list, many=True)
                result_set = {
                    "msg": 'ElectionCenter list is empty' if serializer.data is None else 'Returned ElectionCenter list',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            else:  # Retrieve a specific election center by pk
                election_center = get_object_or_404(ElectionCenter, pk=pk)
                serializer = ElectionCenterSerializer(election_center)
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    @swagger_auto_schema(
        operation_description="Add a new election center",
        request_body=ElectionCenterSerializer,
        responses={201: openapi.Response('')}
    )
    def post(self, request, *args, **kwargs):
        try:
            data = JSONParser().parse(request)
            serializer = ElectionCenterSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "ElectionCenter Added Successfully"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    @swagger_auto_schema(
        operation_description="Update an existing election center",
        request_body=ElectionCenterSerializer,
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the election center to update",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={200: openapi.Response('')}
    )
    def put(self, request, *args, **kwargs):
        try:
            pk = request.query_params.get('pk')
            if pk is None:
                return Response({"msg": "pk is required for updating"}, status=status.HTTP_400_BAD_REQUEST)

            election_center = get_object_or_404(ElectionCenter, pk=pk)
            serializer = ElectionCenterSerializer(election_center, data=request.data)
            if serializer.is_valid():
                serializer.save()
                result_set = {
                    "msg": "Updated ElectionCenter",
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
        operation_description="Delete an election center by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the election center to delete",
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

            election_center = get_object_or_404(ElectionCenter, pk=pk)
            election_center.delete()
            result_set = {
                "msg": "Deleted ElectionCenter",
                "data": None,
            }
            return Response(result_set, status=status.HTTP_200_OK)

        except ElectionCenter.DoesNotExist:
            return Response(
                {"msg": "ElectionCenter not found", "data": None},
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )


class ElectionInfoView(APIView):

    @swagger_auto_schema(
        operation_description="Get all election info or a single election info by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Optional primary key for the election info",
                type=openapi.TYPE_INTEGER,
                required=False
            )
        ],
        responses={200: openapi.Response('')}
    )
    def get(self, request, *args, **kwargs):
        try:
            pk = request.query_params.get('pk')
            if pk is None:  # List all election info
                election_info_list = ElectionInfo.objects.all()
                serializer = ElectionInfoSerializer(election_info_list, many=True)
                result_set = {
                    "msg": 'ElectionInfo list is empty' if serializer.data is None else 'Returned ElectionInfo list',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            else:  # Retrieve a specific election info by pk
                election_info = get_object_or_404(ElectionInfo, pk=pk)
                serializer = ElectionInfoSerializer(election_info)
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    @swagger_auto_schema(
        operation_description="Add a new election info",
        request_body=ElectionInfoSerializer,
        responses={201: openapi.Response('')}
    )
    def post(self, request, *args, **kwargs):
        try:
            data = JSONParser().parse(request)
            serializer = ElectionInfoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "ElectionInfo Added Successfully"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    @swagger_auto_schema(
        operation_description="Update an existing election info",
        request_body=ElectionInfoSerializer,
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the election info to update",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={200: openapi.Response('')}
    )
    def put(self, request, *args, **kwargs):
        try:
            pk = request.query_params.get('pk')
            if pk is None:
                return Response({"msg": "pk is required for updating"}, status=status.HTTP_400_BAD_REQUEST)

            election_info = get_object_or_404(ElectionInfo, pk=pk)
            serializer = ElectionInfoSerializer(election_info, data=request.data)
            if serializer.is_valid():
                serializer.save()
                result_set = {
                    "msg": "Updated ElectionInfo",
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
        operation_description="Delete an election info by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the election info to delete",
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

            election_info = get_object_or_404(ElectionInfo, pk=pk)
            election_info.delete()
            result_set = {
                "msg": "Deleted ElectionInfo",
                "data": None,
            }
            return Response(result_set, status=status.HTTP_200_OK)

        except ElectionInfo.DoesNotExist:
            return Response(
                {"msg": "ElectionInfo not found", "data": None},
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )


class ElectionDataView(APIView):

    @swagger_auto_schema(
        operation_description="Get all election data or a single election data by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Optional primary key for the election data",
                type=openapi.TYPE_INTEGER,
                required=False
            )
        ],
        responses={200: openapi.Response('')}
    )
    def get(self, request, *args, **kwargs):
        try:
            pk = request.query_params.get('pk')
            if pk is None:  # List all election data
                election_data_list = ElectionData.objects.all()
                serializer = ElectionDataSerializer(election_data_list, many=True)
                result_set = {
                    "msg": 'ElectionData list is empty' if serializer.data is None else 'Returned ElectionData list',
                    "data": serializer.data,
                }
                return Response(result_set, status=status.HTTP_200_OK)
            else:  # Retrieve a specific election data by pk
                election_data = get_object_or_404(ElectionData, pk=pk)
                serializer = ElectionDataSerializer(election_data)
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    @swagger_auto_schema(
        operation_description="Add a new election data",
        request_body=ElectionDataSerializer,
        responses={201: openapi.Response('')}
    )
    def post(self, request, *args, **kwargs):
        try:
            data = JSONParser().parse(request)
            serializer = ElectionDataSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "ElectionData Added Successfully"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

    @swagger_auto_schema(
        operation_description="Update an existing election data",
        request_body=ElectionDataSerializer,
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the election data to update",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={200: openapi.Response('')}
    )
    def put(self, request, *args, **kwargs):
        try:
            pk = request.query_params.get('pk')
            if pk is None:
                return Response({"msg": "pk is required for updating"}, status=status.HTTP_400_BAD_REQUEST)

            election_data = get_object_or_404(ElectionData, pk=pk)
            serializer = ElectionDataSerializer(election_data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                result_set = {
                    "msg": "Updated ElectionData",
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
        operation_description="Delete an election data by id",
        manual_parameters=[
            openapi.Parameter(
                'pk',
                openapi.IN_QUERY,
                description="Primary key of the election data to delete",
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

            election_data = get_object_or_404(ElectionData, pk=pk)
            election_data.delete()
            result_set = {
                "msg": "Deleted ElectionData",
                "data": None,
            }
            return Response(result_set, status=status.HTTP_200_OK)

        except ElectionData.DoesNotExist:
            return Response(
                {"msg": "ElectionData not found", "data": None},
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:
            return Response(
                {"msg": str(e), "data": None},
                status=status.HTTP_400_BAD_REQUEST
            )

