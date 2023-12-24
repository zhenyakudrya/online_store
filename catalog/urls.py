from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from catalog.views import home

from catalog.views import contacts

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('catalog.urls')),
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
