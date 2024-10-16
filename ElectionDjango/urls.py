"""
URL configuration for ElectionDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import rest_framework_simplejwt
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Your Project API",
        default_version='v1',
        description="API documentation for your project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourproject.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(rest_framework_simplejwt.authentication.JWTAuthentication,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('Account.urls')),
    path('common/', include('Common.urls')),
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$',
    #         authentication_classes([])(permission_classes([AllowAny])(schema_view.without_ui(cache_timeout=0))),
    #         name='schema-json'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),

    path('swagger/',
         authentication_classes([])(permission_classes([AllowAny])(schema_view.with_ui('swagger', cache_timeout=0))),
         name='schema-swagger-ui'),
    path('redoc/',
         authentication_classes([])(permission_classes([AllowAny])(schema_view.with_ui('redoc', cache_timeout=0))),
         name='schema-redoc'),

]
