from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import UserType
from Account.serializers import UserTypeSerializer


# Create your views here.

@csrf_exempt
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

    except Exception as e:
        return JsonResponse(e)
