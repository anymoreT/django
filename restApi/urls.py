from django.conf.urls import  url
from rest_framework import routers
from .views import RestApiViewSet,RestApiPostViewSet,RestApiView
import pdb


router = routers.DefaultRouter()
router.register('restApi', RestApiViewSet)
router.register('postApi', RestApiPostViewSet)
router.register('restView', RestApiView)

# urlpatterns = [
#     url(r'^docs/', RestApiViewSet),
# ]
urlpatterns = router.urls

