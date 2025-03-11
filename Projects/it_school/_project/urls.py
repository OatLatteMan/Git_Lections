from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('school/', include('school.urls', namespace = 'school')),

    path('sprava/', admin.site.urls),
] + debug_toolbar_urls() + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
