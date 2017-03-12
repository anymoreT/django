from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import  status
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializer import PoemSerializer
from .models import Poem
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


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

@csrf_exempt
def PoemListLimit(request, pk):
    if request.method == "GET":
        poems = Poem.objects.all()
        serialize =  PoemSerializer(poems, many = True)
        return JsonResponse(serialize.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serialize =  PoemSerializer(data = data, many = True)
        if serialize.is_valid():
            serialize.save()
            return JsonResponse(serialize.data, status=201)
        else:
            return JsonResponse(serialize.errors, status=400)


@api_view(['GET'])
def get_peom_by_index(request, pk):
    if request.method == "GET":
        poems = Poem.objects.get(pk=pk)
        serialize =  PoemSerializer(poems, many = True)
        return Response(serialize.data)
