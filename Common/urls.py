from django.urls import path, re_path

from .views import *

urlpatterns = [
    re_path('country/(?P<pk>\d+)?/?$', CountryView.as_view(), name='country'),
    re_path('division/(?P<pk>\d+)?/?$', DivisionView.as_view(), name='division'),
    re_path('district/(?P<pk>\d+)?/?$', DistrictView.as_view(), name='district'),
    re_path('upazila/(?P<pk>\d+)?/?$', UpazilaView.as_view(), name='upazila'),
    re_path('union/(?P<pk>\d+)?/?$', UnionView.as_view(), name='union'),
    re_path('ward/(?P<pk>\d+)?/?$', WardView.as_view(), name='ward'),
    re_path('city_corporation/(?P<pk>\d+)?/?$', CityCorporationView.as_view(), name='city_corporation'),
    re_path('municipality/(?P<pk>\d+)?/?$', MunicipalityView.as_view(), name='municipality'),
    re_path('address/(?P<pk>\d+)?/?$', AddressView.as_view(), name='address'),

]
