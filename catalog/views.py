from django.shortcuts import render

from catalog.models import Category, Product


def contacts(requests):
    return render(requests, 'catalog/contacts.html')


def products(requests):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Наш ассортимент'
    }
    return render(requests, 'catalog/products.html', context)


def home(requests):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Все категории техники'
    }
    return render(requests, 'catalog/home.html', context)


def category_products(requests, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Все наши {category_item.category_name}'
    }
    return render(requests, 'catalog/category_products.html', context)


def product(requests, id):
    product = Product.objects.get(id=id)
    context = {
        'product_name': product.product_name,
        'product_content': product.product_content,
        'title': 'Выбранный товар',
        'product_image': product.product_image,
        'price_for_one': f'Цена: {product.price_for_one} руб.'
    }
    return render(requests, 'catalog/product.html', context)
