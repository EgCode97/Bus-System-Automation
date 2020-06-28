from django.shortcuts import render
import django.http as http


# Create your views here.
def upload(request):
    return http.HttpResponse("HOLA")