from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, contacts, ProductDetailView
from catalog.views import ProductsListView, CategoryProductsListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='index'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/catalog/', CategoryProductsListView.as_view(), name='category_products'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),
]
