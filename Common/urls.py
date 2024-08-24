from django.urls import path

from .views import *

urlpatterns = [

    path('usertype_list/', usertype_list, name='usertype_list'),
    path('usertype_list/?<int:pk>/', usertype_list, name='usertype_list')

]
