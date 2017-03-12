from django.conf.urls import  url
from . import views

urlpatterns = [
                url('^poem/$', views.PoemListView.as_view(), name = "poem_list"),
                url('^poem-limit/$', views.PoemListLimitView.as_view(), name = "poem_list"),
                url('^doc/$', views.schema_view)
              ]