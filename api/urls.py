from django.conf.urls import  url
from . import views

urlpatterns = [
                url('^poem/$', views.PoemListView.as_view(), name = "poem_list"),
              ]