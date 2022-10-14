import pytest

from organizations.models import Product


class TestProductAPI:

    @pytest.mark.django_db(transaction=True)
    def test_product_not_found(self, user_client, product_1):
        response = user_client.get(f'/api/products/{product_1.id}/')

        assert response.status_code != 404, (
            'Страница `/api/products/{product_1.id}/` не найдена, проверьте этот адрес в *urls.py*'
        )

    @pytest.mark.django_db(transaction=True)
    def test_products_not_authenticated(self, client):
        response = client.get(f'/api/products/')

        assert response.status_code == 401, (
            'Страница `/api/products/` должна быть доступна по токену.'
        )

    @pytest.mark.django_db(transaction=True)
    def test_products_get(self, user_client, product_1):
        response = user_client.get('/api/products/')

        assert response.status_code != 404, (
            'Страница `/api/products/` не найдена, проверьте этот адрес в *urls.py*'
        )

        test_data = response.json()
        assert type(test_data) == list, (
            'Проверьте, что при GET запросе на `/api/products/` возвращается список'
        )

        assert len(test_data) == Product.objects.count(), (
            'Проверьте, что при GET запросе на `/api/products/` возвращается весь список продуктов'
        )

        product = Product.objects.all()[0]
        test_product = test_data[0]
        assert 'id' in test_product, (
            'Проверьте, что добавили `id` в список полей `fields` сериализатора модели Product'
        )
        assert 'name' in test_product, (
            'Проверьте, что добавили `name` в список полей `fields` сериализатора модели Product'
        )
        assert 'category' in test_product, (
            'Проверьте, что добавили `category` в список полей `fields` сериализатора модели Product'
        )

        assert test_product['id'] == product.id, (
            'Проверьте, что при GET запросе на `/api/products/` возвращается id продукта'
        )

        assert test_product['name'] == product.name, (
            'Проверьте, что при GET запросе на `/api/products/` возвращается название продукта'
        )

    @pytest.mark.django_db(transaction=True)
    def test_post_create(self, user_client):
        product_count = Product.objects.count()

        data = {}
        response = user_client.post('/api/products/', data=data)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе на `/api/products/` с не правильными данными возвращается статус 400'
        )

        data = {'name': 'Продукт_тест', 'category': {'name': 'Тестовая категория',}}
        response = user_client.post('/api/products/', data=data, format="json")
        assert response.status_code == 201, (
            'Проверьте, что при POST запросе на `/api/products/` с правильными данными возвращается статус 201'
        )

        test_data = response.json()

        msg_error = (
            'Проверьте, что при POST запросе на `/api/products/` возвращается словарь с данными нового продукта'
        )
        assert type(test_data) == dict, msg_error
        assert test_data.get('name') == data['name'], msg_error

        assert product_count + 1 == Product.objects.count(), (
            'Проверьте, что при POST запросе на `/api/products/` создается продукт'
        )