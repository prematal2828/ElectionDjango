from django.urls import path
from .views import *

urlpatterns = [
    path('user_login/', user_login, name='user_login'),
    path('usertype_list/', usertype_list, name='usertype_list'),
    path('usertype_list/?<int:pk>/', usertype_list, name='usertype_list')
]
