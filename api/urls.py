from django.conf.urls import  url
from . import views

urlpatterns = [
                url('^poem/$', views.PoemListView.as_view(), name = "poem_list"),
                url('^poem/t([0-9]+)/$', views.PoemListLimit, name = "poem_list"),
                url('^poem/(?P<pk>[0-9]+)/$', views.get_peom_by_index, name="poem_list"),
                url('^doc/$', views.schema_view)
              ]