from django.urls import path, re_path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *

urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('user_login/', UserLoginView.as_view(), name='user_login'),
    path('user_login/', authentication_classes([])(permission_classes([AllowAny])(UserLoginView)).as_view(),
         name='user_login'),

    path('user_logout/', UserLogoutView.as_view(), name='user_logout'),

    # path('usertype/', UserTypeView.as_view(), name='usertype'),
    re_path(r'^usertype/(?P<pk>\d+)?/?$', UserTypeView.as_view(), name='usertype'),


    # path('user/', UserView.as_view(), name='user'),
    re_path(r'^user/(?P<pk>\d+)?/?$', UserView.as_view(), name='user'),

]
