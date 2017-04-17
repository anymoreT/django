from django.conf.urls import  url
from blog import views
import  pdb

urlpatterns = [
                url('index', views.index),

              ]
