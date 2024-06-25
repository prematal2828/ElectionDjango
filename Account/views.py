from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import UserType
from Account.serializers import UserTypeSerializer


# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def usertype_list(request, id=None):
    try:
        if id == None:
            if request.method == 'GET':
                usertypes = UserType.objects.all()
                serializer = UserTypeSerializer(usertypes, many=True)
                return JsonResponse(serializer.data, safe=False)
            if request.method == 'POST':
                data = JSONParser().parse(request)
                serializer = UserTypeSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse("User Type Added Successfully", safe=False)
        else:
            if request.method == 'GET':
                usertype = UserType.objects.get(pk=id)
                serializer = UserTypeSerializer(usertype, many=False)
                return JsonResponse(serializer.data, safe=False)
            elif request.method == 'PUT':
                data = JSONParser().parse(request)
                serializer = UserTypeSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse("User Type Updated Successfully", safe=False)
            elif request.method == 'DELETE':
                usertype = UserType.objects.get(pk=id)
                usertype.delete()
                return JsonResponse("User Type Deleted Successfully", safe=False)


    except Exception as e:
        return JsonResponse(e)
