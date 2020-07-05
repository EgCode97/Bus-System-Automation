from django.shortcuts import render
import django.http as http
from django.views.decorators.csrf import csrf_exempt

from .models import BusStop, BusUnit, Route
from Bus_automation.settings import UPLOAD_PASSWORD, DECRIPTION_KEY


from cryptography.fernet import Fernet

# Create your views here.
@csrf_exempt
def upload(request):
    data = {
        'name': 'Elias',
        'lastname': 'Colmenarez',
        'age': 23
    }

    if request.method == 'POST':
        #posted_data = request.POST.dict()
        posted_data = request.POST.dict()

        
        fernet = Fernet(DECRIPTION_KEY)

        pass_encrypted =  posted_data['token'].encode()

        print("PASS ENCRYPTED->", pass_encrypted)
        password = fernet.decrypt(pass_encrypted).decode()
        print("PASSWORD->", password)


        print("HACIENDO POST->", posted_data)

        if password == UPLOAD_PASSWORD:
            print("CONTRASEÑA CORRECTA\n\n")

            unit = BusUnit.objects.get(id= posted_data['id'])
            current_location = BusStop.objects.get(name= posted_data['current_location'])
            unit.location = current_location
            unit.save()
    return http.JsonResponse(data)