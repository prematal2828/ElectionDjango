from django.urls import path

from .views import *

urlpatterns = [
    path('country_list/', country_list, name='country_list'),
    path('division_list/', division_list, name='division_list'),

]
