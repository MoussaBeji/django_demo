from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello Moussa this is music hoomepage</h1><br> <h2> my first git test</h2>")
