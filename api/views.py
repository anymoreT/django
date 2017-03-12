from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import  status
from rest_framework.response import Response
from .serializer import PoemSerializer
from .models import Poem

from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Pastebin API')
# Create your views here.
class PoemListView(APIView):
    def get(self, request, format = None):
        poems = Poem.objects.all()
        serialize =  PoemSerializer(poems, many = True)
        return Response(serialize.data)

    def post(self, request, format=None):
        serialize =  PoemSerializer(data = request.data, many = True)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status.HTTP_201_CREATED)
        else:
            return Response(serialize.errors, status = status.HTTP_400_BAD_REQUEST)


class PoemListLimitView(APIView):
    def get(self, request, format = None):
        poems = Poem.objects.all()
        serialize =  PoemSerializer(poems, many = True)
        return Response(serialize.data)

    def post(self, request, format=None):
        serialize =  PoemSerializer(data = request.data, many = True)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status.HTTP_201_CREATED)
        else:
            return Response(serialize.errors, status = status.HTTP_400_BAD_REQUEST)