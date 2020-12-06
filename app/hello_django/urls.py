from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from upload import views
from upload.views import image_upload

urlpatterns = [
    path("", image_upload, name="upload"),
    url(r'^save_to_redis/$', views.save_to_redis, name='save_to_redis'),
    url(r'^sync_endpoint/$', views.endpoint, name='endpoint'),
    url(r'^write_to_db/$', views.write_to_db, name='write_to_db'),
    path("admin/", admin.site.urls),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
