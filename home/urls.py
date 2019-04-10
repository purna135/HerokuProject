from django.conf.urls import url
from . import views
from HerokuProject import settings
from django.views.static import serve

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^receive-images/$', views.ReceiveImages.as_view(), name='receive-image'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
]