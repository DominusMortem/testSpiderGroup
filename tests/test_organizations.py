import pytest

from organizations.models import Organization

class TestOrganizationAPI:

    @pytest.mark.django_db(transaction=True)
    def test_districts_not_found(self, user_client):
        response = user_client.get('/api/districts/')

        assert response.status_code != 404, (
                'Страница `/api/districts/` не найдена, проверьте этот адрес в *urls.py*'
        )

    @pytest.mark.django_db(transaction=True)
    def test_districts_not_authenticated(self, client):
        response = client.get(f'/api/districts/')

        assert response.status_code == 401, (
            'Страница `/api/districts/` должна быть доступна по токену.'
        )

    @pytest.mark.django_db(transaction=True)
    def test_district_not_found(self, user_client, district_1):
        response = user_client.get(f'/api/districts/{district_1.id}')

        assert response.status_code != 404, (
            'Страница `/api/districts/{district_1.id}` не найдена, проверьте этот адрес в *urls.py*'
        )

    @pytest.mark.django_db(transaction=True)
    def test_organization_not_found(self, user_client, district_1,
                                     organization_1):
        response = user_client.get(
            f'/api/districts/{district_1.id}/organizations/{organization_1.id}/', )

        assert response.status_code != 404, (
            f'Страница `/api/districts/{district_1.id}/organizations/{organization_1.id}/` не найдена, проверьте этот адрес в *urls.py*'
        )

    @pytest.mark.django_db(transaction=True)
    def test_organizations_not_authenticated(self, client, district_1):
        response = client.get(f'/api/districts/{district_1.id}/organizations/', )

        assert response.status_code == 401, (
            f'Страница `/api/districts/{district_1.id}/organizations/` должна быть доступна по токену.'
        )

    @pytest.mark.django_db(transaction=True)
    def test_organizations_get(self, user_client, district_1, organization_1):
        response = user_client.get(f'/api/districts/{district_1.id}/organizations/', )

        assert response.status_code != 404, (
            f'Страница `/api/districts/{district_1.id}/organizations/` не найдена, проверьте этот адрес в *urls.py*'
        )

        test_data = response.json()
        assert type(test_data) == list, (
            'Проверьте, что при GET запросе на `/api/districts/{district_1.id}/organizations/` возвращается список'
        )

        assert len(test_data) == Organization.objects.count(), (
            'Проверьте, что при GET запросе на `/api/districts/{district_1.id}/organizations/` возвращается весь список продуктов'
        )

        organization = Organization.objects.all()[0]
        test_organization = test_data[0]

        assert 'id' in test_organization, (
            'Проверьте, что добавили `id` в список полей `fields` сериализатора модели Organization'
        )
        assert 'name' in test_organization, (
            'Проверьте, что добавили `name` в список полей `fields` сериализатора модели Organization'
        )
        assert 'description' in test_organization, (
            'Проверьте, что добавили `description` в список полей `fields` сериализатора модели Organization'
        )
        assert 'network' in test_organization, (
            'Проверьте, что добавили `network` в список полей `fields` сериализатора модели Organization'
        )
        assert 'district' in test_organization, (
            'Проверьте, что добавили `district` в список полей `fields` сериализатора модели Organization'
        )
        assert 'product' in test_organization, (
            'Проверьте, что добавили `product` в список полей `fields` сериализатора модели Organization'
        )
        assert test_organization['id'] == organization.id, (
            'Проверьте, что при GET запросе на `/api/districts/{district_1.id}/organizations/` возвращается id организации'
        )
        assert test_organization['name'] == organization.name, (
            'Проверьте, что при GET запросе на `/api/districts/{district_1.id}/organizations/` возвращается имя организации'
        )
        assert test_organization['description'] == organization.description, (
            'Проверьте, что при GET запросе на `/api/districts/{district_1.id}/organizations/` возвращается описание организации'
        )

    @pytest.mark.django_db(transaction=True)
    def test_organizations_search(self, user_client, district_1, organization_1, organization_2):
        response = user_client.get(
            f'/api/districts/{district_1.id}/organizations/?search=Продукт 1', )

        test_data = response.json()
        organization = Organization.objects.filter(product__product__name='Продукт 1')

        assert len(test_data) == len(organization), (
            'Количество организаций не совпадает'
        )

        assert test_data[0]['id'] == organization[0].id, (
            'Поиск по названию продукта работает не верно')
