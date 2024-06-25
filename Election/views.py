from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import UserType
from .serializers import UserTypeSerializer , TestUserSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

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








@api_view(['GET'])
def testView(request):
    person = {
        'name':'Rakibul Hasan',
        'APItype':'minimal'
    }
    return Response(person);


@api_view(['GET'])
def userList(request):
    userData = UserType.objects.all()
    serializer = UserTypeSerializer(userData, many=True)
    return Response(serializer.data);