from django.core.validators import MinValueValidator
from django.db import models


PRODUCT_MIN_PRICE = 1


class DistrictCity(models.Model):
    name = models.CharField('Название', max_length=30)

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('Название', max_length=30)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class NetworkEnterprises(models.Model):
    name = models.CharField('Название', max_length=30)

    class Meta:
        verbose_name = 'Сеть предприятий'
        verbose_name_plural = 'Сеть предприятий'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Название', max_length=30)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} ({self.category})'


class PriceProduct(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    price = models.PositiveIntegerField(
        'Цена',
        validators=(
            MinValueValidator(
                PRODUCT_MIN_PRICE,
                message='Цена не может быть меньше 1!',
            ),
        )
    )

    class Meta:
        verbose_name = 'Цена товара'
        verbose_name_plural = 'Цена товаров'
        constraints = (
            models.UniqueConstraint(
                fields=('product', 'price',),
                name='unique_product_price',
            ),
        )

    def __str__(self):
        return (
            f'{self.product} -'
            f' {self.price}'
        )


class Organization(models.Model):
    name = models.CharField('Предприятие', max_length=30)
    description = models.TextField('Описание')
    network = models.ForeignKey(
        NetworkEnterprises,
        on_delete=models.CASCADE,
        verbose_name='Сеть предприятий'
    )
    product = models.ManyToManyField(
        PriceProduct,
        related_name='organizations',
        verbose_name='Продукты'
    )
