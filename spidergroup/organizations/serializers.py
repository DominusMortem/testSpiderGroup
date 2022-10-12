from django.shortcuts import get_object_or_404
from rest_framework.serializers import ModelSerializer

from .models import (
    DistrictCity,
    Category,
    NetworkEnterprises,
    Product,
    PriceProduct,
    Organization
)


class DistrictCitySerializer(ModelSerializer):

    class Meta:
        model = DistrictCity
        fields = '__all__'


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class NetworkEnterprisesSerializer(ModelSerializer):

    class Meta:
        model = NetworkEnterprises
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'category',)


class PriceProductSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = PriceProduct
        fields = ('id', 'product')


class OrganizationSerializer(ModelSerializer):
    network = NetworkEnterprisesSerializer()
    district = DistrictCitySerializer(many=True)
    product = PriceProductSerializer(many=True)

    class Meta:
        model = Organization
        fields = ('id', 'name', 'network', 'district', 'product')