from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from Account.serializers import *
from Account.models import checkBlacklistedAccessTokens


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes((JWTAuthentication,))
@permission_classes((IsAuthenticated,))
def usertype_list(request):
    try:
        if checkBlacklistedAccessTokens(request) is False:
            pk = request.query_params.get('pk')
            if pk == None:
                if request.method == 'GET':
                    userTypes = UserType.objects.all()
                    serializer = UserTypeSerializer(userTypes, many=True)

                    resultSet = {
                        "msg": 'Returned User Types list',
                        "data": serializer.data,
                    }

                    return Response(resultSet, status=status.HTTP_200_OK)
                if request.method == 'POST':
                    data = JSONParser().parse(request)
                    serializer = UserTypeSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response("User Type Added Successfully")
            else:
                userTypes = UserType.objects.get(pk=pk)
                if request.method == 'GET':
                    serializer = UserTypeSerializer(userTypes, many=False)
                    return Response(serializer.data)
                elif request.method == 'PUT':
                    serializer = UserTypeSerializer(userTypes, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        resultSet = {
                            "msg": 'Updated User Type',
                            "data": serializer.data,
                        }

                        return Response(resultSet, status=status.HTTP_200_OK)
                elif request.method == 'DELETE':
                    userTypes.delete()
                    resultSet = {
                        "msg": 'Deleted User Type',
                        "data": None,
                    }
                    return Response(resultSet, status=status.HTTP_200_OK)

        else:
            resultSet = {
                "msg": 'User Logged Out',
                "data": None,
            }
            return Response(resultSet, status=status.HTTP_200_OK)

    except Exception as e:
        resultSet = {
            "msg": e,
            "data": None,
        }
        return Response(resultSet, status=status.HTTP_400_BAD_REQUEST)
