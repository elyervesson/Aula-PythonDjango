# -*- encoding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse #irá conter uma resposta do tipo HTTP

def index(request):
    return HttpResponse(u"Olá mundo")
