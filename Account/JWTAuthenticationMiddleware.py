from django.contrib.auth import logout
from django.http import JsonResponse
from django.urls import resolve
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from Account.models import checkBlacklistedAccessTokens, BlacklistedAccessTokens


class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        excluded_paths = ['/', 'account/user_login/', 'account/api/token/', 'account/api/token/refresh/', 'swagger/',
                          'redoc/', ]
        current_path = resolve(request.path_info).route

        if current_path in excluded_paths:
            try:
                return self.get_response(request)
            except Exception as e:
                return e

        access_token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        jwt_auth = JWTAuthentication()
        try:
            jwt_auth.authenticate(request)
        except (InvalidToken, TokenError):
            return JsonResponse({"msg": "Unauthorized Access", "data": None}, status=401)

        if checkBlacklistedAccessTokens(request) or not request.user.is_authenticated or access_token == '':
            if access_token != '' and not BlacklistedAccessTokens.objects.filter(access_token=access_token).exists():
                blacklist_access_token = BlacklistedAccessTokens(access_token=access_token)
                blacklist_access_token.save()
            logout(request)
            return JsonResponse({"msg": "Unauthorized Access", "data": None}, status=401)

        return self.get_response(request)
