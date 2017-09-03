from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Handle path '/'
    url(r'^$', views.hello, name = 'hello'),
]
