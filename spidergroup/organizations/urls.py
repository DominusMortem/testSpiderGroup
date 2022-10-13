from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    OrganizationViewSet,
    DistrictCityViewSet,
    ProductViewSet
)

router = DefaultRouter()
router.register('districts', DistrictCityViewSet, basename='districts')
router.register(
    r'districts/(?P<district_id>\d+)/organizations',
    OrganizationViewSet,
    basename='organizations'
)
router.register('products', ProductViewSet, basename='products')

app_name = 'organizations'

urlpatterns = [
    path('', include(router.urls)),
]
