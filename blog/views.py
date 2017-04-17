from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page
from django.conf import settings
import pdb

# Create your views here.

def index(req):
    return render_to_response('index1.html')