from django.urls import path

from .views import *

urlpatterns = [
    path('country_list/', country_list, name='country_list'),
    path('division_list/', division_list, name='division_list'),
    path('district_list/', district_list, name='district_list'),
    path('division_list/', division_list, name='division_list'),
    path('upazila_list/', upazila_list, name='upazila_list'),
    path('union_list/', union_list, name='union_list'),
    path('ward_list/', ward_list, name='ward_list'),
    path('city_corporation_list/', city_corporation_list, name='city_corporation_list'),
    path('municipality_list/', municipality_list, name='municipality_list'),
    path('address_list/', address_list, name='address_list'),

]
