from rest_framework.serializers import ModelSerializer

from .models import (
    DistrictCity,
    Category,
    NetworkEnterprises,
    Product,
    PriceProduct,
    Organization
)


class NetworkEnterprisesSerializer(ModelSerializer):

    class Meta:
        model = NetworkEnterprises
        fields = ('id', 'name')


class DistrictCitySerializer(ModelSerializer):

    class Meta:
        model = DistrictCity
        fields = '__all__'


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'category',)

    def create(self, validated_data):
        category = validated_data.pop('category')
        category, *_ = Category.objects.get_or_create(**category)
        product, *_ = Product.objects.get_or_create(
            category=category,
            **validated_data
        )
        return product


class PriceProductSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = PriceProduct
        fields = ('id', 'product', 'price',)


class OrganizationSerializer(ModelSerializer):
    network = NetworkEnterprisesSerializer()
    district = DistrictCitySerializer(many=True)
    product = PriceProductSerializer(many=True)

    class Meta:
        model = Organization
        fields = ('id', 'name', 'description', 'network', 'district', 'product',)
