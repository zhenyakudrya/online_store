from django.core.management import BaseCommand
import json

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        Category.objects.all().delete()

        category_list = [
            {'category_name': 'Телефон'},
            {'category_name': 'Компьютер'},
            {'category_name': 'Телевизор'},
            {'category_name': 'Холодильник'},
            {'category_name': 'Пылесос'},
        ]
        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(category_for_create)

        Product.objects.all().delete()

        products_list = [
            {'product_name': 'Iphone 15', 'category': Category(category_name='Телефон'), 'price': '5'},
            {'product_name': 'Macbook', 'category': Category(category_name='Компьютер'), 'price': '10'},
            {'product_name': 'LG', 'category': Category(category_name='Телевизор'), 'price': '8'},
            {'product_name': 'Beko', 'category': Category(category_name='Холодильник'), 'price': '5'},
            {'product_name': 'Tefal', 'category': Category(category_name='Пылесос'), 'price': '3'},
        ]

        product_for_create = []
        for product_item in products_list:
            product_for_create.append(
                Product(**product_item)
            )
        Product.objects.bulk_create(product_for_create)