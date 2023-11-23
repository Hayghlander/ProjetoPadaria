from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

admin.site.site_header = "Padoca do Hay"
admin.site.site_title = "Padoca do Hay"
admin.site.index_title = "Sistema de gerenciamento de padaria"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)