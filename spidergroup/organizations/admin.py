from django.contrib.admin import site, ModelAdmin, display, register

from .models import (
    DistrictCity,
    Category,
    NetworkEnterprises,
    Product,
    PriceProduct,
    Organization
)

site.register(DistrictCity)
site.register(Category)
site.register(NetworkEnterprises)
site.register(Product)


@register(PriceProduct)
class PriceProductAdmin(ModelAdmin):
    list_display = ('get_product', 'get_category', 'price',)
    search_fields = ('get_product',)
    ordering = ('price',)

    @display(description='Продукт')
    def get_product(self, obj):
        return obj.product.name

    @display(description='Категория')
    def get_category(self, obj):
        return obj.product.category.name


@register(Organization)
class OrganizationAdmin(ModelAdmin):
    list_display = ('name', 'description', 'network',)
    list_filter = ('name', 'network', 'product',)
