from django.conf.urls import  url
from online import views

urlpatterns = [
                url('login', views.login),
                url('regist', views.regist),
                url('index', views.index),
                url('logout', views.logout),
              ]
