from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product
# from catalog.views import contacts
from catalog.views import products, category_products

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='index'),
    path('products/', products, name='products'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/catalog/', category_products, name='category_products'),
    path('<int:id>/product/', product, name='product'),
]
