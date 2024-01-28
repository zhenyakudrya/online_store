from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование')
    product_content = models.TextField(verbose_name='описание')
    product_image = models.ImageField(upload_to='catalog/', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price_for_one = models.IntegerField(verbose_name='цена')
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_change = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='пользователь')

    def __str__(self):
        return f'{self.product_name} {self.product_content}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='наименование')
    category_content = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Version(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='имя версии')
    current_version_indicator = models.BooleanField(default=True, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.product, self.version_name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
