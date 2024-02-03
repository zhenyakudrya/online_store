from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, contacts, ProductDetailView
from catalog.views import ProductsListView, CategoryProductsListView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='index'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/catalog/', CategoryProductsListView.as_view(), name='category_products'),
    path('<int:pk>/product/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('<int:pk>/catalog/create', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/catalog/edit', ProductUpdateView.as_view(), name='edit'),
]
