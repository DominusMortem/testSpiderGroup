import pytest


@pytest.fixture
def district_1():
    from organizations.models import DistrictCity
    return DistrictCity.objects.create(name='Район 1')


@pytest.fixture
def district_2():
    from organizations.models import DistrictCity
    return DistrictCity.objects.create(name='Район 2')


@pytest.fixture
def category_1():
    from organizations.models import Category
    return Category.objects.create(name='Категория 1')


@pytest.fixture
def category_2():
    from organizations.models import Category
    return Category.objects.create(name='Категория 2')


@pytest.fixture
def network_1():
    from organizations.models import NetworkEnterprises
    return NetworkEnterprises.objects.create(name='Сеть 1')


@pytest.fixture
def network_2():
    from organizations.models import NetworkEnterprises
    return NetworkEnterprises.objects.create(name='Сеть 2')


@pytest.fixture
def product_1(category_1):
    from organizations.models import Product
    return Product.objects.create(name='Продукт 1', category=category_1)


@pytest.fixture
def product_2(category_2):
    from organizations.models import Product
    return Product.objects.create(name='Продукт 2', category=category_2)


@pytest.fixture
def price_1(product_1):
    from organizations.models import PriceProduct
    return PriceProduct.objects.create(product=product_1, price=20)


@pytest.fixture
def price_2(product_2):
    from organizations.models import PriceProduct
    return PriceProduct.objects.create(product=product_2, price=30)


@pytest.fixture
def price_3(product_2):
    from organizations.models import PriceProduct
    return PriceProduct.objects.create(product=product_2, price=10)


@pytest.fixture
def organization_1(network_1, district_1, price_1):
    from organizations.models import Organization
    organization = Organization.objects.create(
        name='Организация 1',
        description='Тестовое описание',
        network=network_1,
    )
    organization.district.add(district_1)
    organization.product.add(price_1)
    return organization


@pytest.fixture
def organization_2(network_1, district_1, district_2, price_2, price_3):
    from organizations.models import Organization
    organization= Organization.objects.create(
        name='Организация 1',
        description='Тестовое описание',
        network=network_1,
    )
    organization.district.add(*[district_1, district_2])
    organization.product.add(*[price_2, price_3])
    return organization
