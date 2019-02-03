from django.conf.urls import url
from second_app import views


urlpatterns =[
    url(r'^$', views.second_app_main, name='second_app_main'),
    url(r'forms/', views.second_app_main_forms, name='second_app_main_forms')
]
