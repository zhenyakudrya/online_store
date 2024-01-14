from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Category, Product


def contacts(requests):
    return render(requests, 'catalog/contacts.html')


class ProductsListView(ListView):
    model = Product
    extra_context = {
        'title': 'Наш ассортимент'
    }


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Все категории техники'
    }


class CategoryProductsListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f'Все наши {category_item.category_name}'

        return context_data


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


# class ProductDetailView(DetailView):
#     model = Product
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         # queryset = queryset.filter(id=self.kwargs.get('id'))
#         return queryset
#
#     def get_context_data(self, *args, **kwargs):
#         context_data = super().get_context_data(*args, **kwargs)
#
#         product = Product.objects.get(id=self.kwargs.get('id'))
#         context_data['product_name'] = product.product_name
#         context_data['product_content'] = product.product_content
#         context_data['title'] = 'Выбранный товар'
#         context_data['product_image'] = product.product_image
#         context_data['price_for_one'] = f'Цена: {product.price_for_one} руб.'
#
#         return context_data
