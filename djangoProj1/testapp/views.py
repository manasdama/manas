from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display_view(request):
    data="<h1>This Django Project</h1>"
    return HttpResponse(data)
