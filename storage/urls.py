import django.conf
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('medical_card.urls')),
]

admin.site.site_header = "Medical card"
admin.site.site_title = "Управление данными"
admin.site.index_title = "Интерфейс врача"

if django.conf.settings.DEBUG:  # new
    urlpatterns += static(django.conf.settings.MEDIA_URL, document_root=django.conf.settings.MEDIA_ROOT)
