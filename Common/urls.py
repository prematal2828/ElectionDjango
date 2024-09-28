from django.urls import path

from .views import *

urlpatterns = [
    path('country/', CountryView.as_view(), name='country'),
    path('division/', DivisionView.as_view(), name='division'),
    path('district/', DistrictView.as_view(), name='district'),
    path('upazila/', UpazilaView.as_view(), name='upazila'),
    path('union/', UnionView.as_view(), name='union'),
    path('ward/', WardView.as_view(), name='ward'),
    path('city_corporation/', CityCorporationView.as_view(), name='city_corporation'),
    path('municipality/', MunicipalityView.as_view(), name='municipality'),
    path('address/', AddressView.as_view(), name='address'),

]
