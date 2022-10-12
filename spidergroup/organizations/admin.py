from django.contrib.admin import ModelAdmin, display, register
from django.db.models import Count, Sum

from .models import (
DistrictCity,
Category,
NetworkEnterprises,
Product,
PriceProduct,
Organization
)


register(DistrictCity)
register(Category)
register(NetworkEnterprises)
register(Product)


@register(PriceProduct)
class PriceProductAdmin(ModelAdmin):
    list_display = ('id', 'get_product', 'get_category', 'get_organizations', 'price',)
    list_filter = ('get_product', 'get_category', 'get_organizations')
    search_fields = ('get_product',)
    ordering = ('price',)

    @display(description='Продукт')
    def get_product(self, obj):
        return obj.product.name

    @display(description='Категория')
    def get_category(self, obj):
        return obj.product.category.name

    @display(description='Организация')
    def get_organizations(self, obj):
        return obj.organizations.name


@register(Organization)
class OrganizationAdmin(ModelAdmin):
    list_display = ('name', 'description', 'network', 'product')
    list_filter = ('name', 'network', 'product',)
