from django.shortcuts import render
from rest_framework import viewsets

from .models import RestApi
from .serializer import RestApiSerializer,PostSerializer
from rest_framework.views import APIView

class RestApiViewSet(viewsets.ModelViewSet):
    queryset = RestApi.objects.all()
    serializer_class = RestApiSerializer

class RestApiPostViewSet(viewsets.GenericViewSet):
    queryset = RestApi.objects.all()
    serializer_class = PostSerializer

class RestApiView(APIView):
    queryset = RestApi.objects.all()
    serializer_class = RestApiSerializer
    # def login(username,password):
    #     pass
    # def register(phone,password,email):
    #     pass

