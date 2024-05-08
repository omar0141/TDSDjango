from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from Booking.view import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("Booking.urls")),
    re_path(r".*", index),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
