from django.conf.urls import url, include # Notice we added include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'register$', views.register),
    url(r'login$', views.login),
    url(r'main$', views.main),
    url(r'logout$', views.logout)
    # url(r'main$', views.main)
]