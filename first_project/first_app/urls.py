from django.conf.urls import url
from first_app import views


urlpatterns = [
    url(r'^$', views.first_app_main, name='first_app_main'),
]
