from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from .mixins import ListRetrieveViewSet
from .serializers import (
    OrganizationSerializer,
    DistrictCitySerializer,
    ProductSerializer
)
from .models import DistrictCity, Product


class DistrictCityViewSet(ListRetrieveViewSet):
    serializer_class = DistrictCitySerializer
    queryset = DistrictCity.objects.all()
    permission_classes = (IsAuthenticated,)
    http_method_names = ('get',)


class OrganizationViewSet(ListRetrieveViewSet):
    serializer_class = OrganizationSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ('get',)
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('product__product__name',)
    ordering_fields = ('product__price', 'product__product__category__name', )

    def get_queryset(self):
        district = get_object_or_404(
            DistrictCity,
            id=self.kwargs.get('district_id')
        )
        return district.organizations.all()


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'post',)
