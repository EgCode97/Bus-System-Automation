from django.shortcuts import render
import django.http as http


# Create your views here.
def upload(request):
    data = {
        'name': 'Elias',
        'location': 'Colmenarez',
        'age': 23
    }

    print(request)
    return http.JsonResponse(data)