
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from analysis import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)