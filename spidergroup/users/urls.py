from django.urls import include, path
from djoser.views import TokenDestroyView, TokenCreateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

authorization = [
    path(
        'token/login/',
        TokenCreateView.as_view(),
        name='login',
    ),
    path('token/logout/', TokenDestroyView.as_view(), name='logout'),
]

app_name = 'users'

urlpatterns = [
    path('', include(authorization)),
]
