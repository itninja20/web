from django.shortcuts import render

# Create your views here.

import json
from django.http import HttpResponse

from django.views.generic import ListView
#from django.http import JsonResponse
from django.http.response import JsonResponse
from .models import Fachtest
from django.core import serializers


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def server_list(request):
    #data = [{'name': 'Peter', 'email': 'peter@example.org'},
    #        {'name': 'Julia', 'email': 'julia@example.org'}]

    data = Fachtest.objects.all() #.filter(fqdn='batch-ft1.corp.int')
    d = serializers.serialize('json', data)
    return HttpResponse(d, content_type="application/json")


