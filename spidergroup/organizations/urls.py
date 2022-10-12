from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    OrganizationViewSet
)

router = DefaultRouter()
router.register('organizations', OrganizationViewSet, basename='organizations')

app_name = 'organizations'

urlpatterns = [
    path('', include(router.urls)),
]
