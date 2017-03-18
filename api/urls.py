from django.conf.urls import  url
from . import views

from rest_framework import routers
from .views1 import StudentViewSet, UniversityViewSet, schema_view
#
# urlpatterns = [
#                 url('^poem/$', views.PoemListView.as_view(), name = "poem_list"),
#                 url('^poem/t([0-9]+)/$', views.PoemListLimit, name = "poem_list"),
#                 url('^poem/(?P<pk>[0-9]+)/$', views.get_peom_by_index, name="poem_list"),
#                 url('^poem/c([0-9]+)/$', views.create_peom, kwargs={"a":1, "b":2}, name="poem_list"),
#                 url('^doc/$', views.schema_view),
#
#               ]


router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)

urlpatterns = [
    url(r'^docs/', schema_view),
]

urlpatterns += router.urls