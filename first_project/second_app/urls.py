from django.conf.urls import url
from second_app import views

# TEMPLATE TAGGING
app_name = 'second_app'

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),

    # url(r'devices/', views.second_app_devices, name='second_app_devices'),
    url(r'devices/', views.SecondAppDeviceListView.as_view(), name='second_app_devices'),

    url(r'users/', views.second_app_users, name='second_app_users'),
    url(r'forms/', views.second_app_forms, name='second_app_forms')
]
