from django.shortcuts import render
from django.http import HttpResponse


# index views
def index(request):
    return HttpResponse("Возможно здесь будет доска")

