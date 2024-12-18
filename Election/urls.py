
from django.urls import path
from .views import *

urlpatterns = [
    path('election_type/', ElectionTypeView.as_view(), name='election_type'),
    path('election_center/', ElectionCenterView.as_view(), name='election_center'),
    path('election_info/', ElectionInfoView.as_view(), name='election_info'),
    path('election_data/', ElectionDataView.as_view(), name='election_data'),
    path('election_seat/', ElectionSeatView.as_view(), name='election_seat'),
    path('election_details/', ElectionDetailView.as_view(), name='election_details'),
]

