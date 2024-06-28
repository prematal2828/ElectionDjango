from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import UserType
from Account.serializers import UserTypeSerializer


# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def usertype_list(request):
    pk = request.query_params.get('pk')
    try:
        if pk == None:
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
            usertype = UserType.objects.get(pk=pk)
            if request.method == 'GET':
                serializer = UserTypeSerializer(usertype, many=False)
                return JsonResponse(serializer.data, safe=False)
            elif request.method == 'PUT':
                serializer = UserTypeSerializer(usertype, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse("User Type Updated Successfully", safe=False)
            elif request.method == 'DELETE':
                usertype.delete()
                return JsonResponse("User Type Deleted Successfully", safe=False)


    except Exception as e:
        return JsonResponse("Data Not Found", safe=False)
        # return JsonResponse(e)
