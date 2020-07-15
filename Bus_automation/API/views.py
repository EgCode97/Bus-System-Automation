from django.shortcuts import render
import django.http as http
from django.views.decorators.csrf import csrf_exempt

from .models import BusStop, BusUnit, Route
from Bus_automation.settings import UPLOAD_PASSWORD, DECRIPTION_KEY


from cryptography.fernet import Fernet
import datetime

# Create your views here.
@csrf_exempt
def upload(request):
    dato_prueba = {
        'name': 'Elias',
        'lastname': 'Colmenarez',
        'age': 23
    }

    if request.method == 'PUT':
        print("HACIENDO PUT")

        raw_data = request.body
        key = raw_data[:44]
        encrypted_data = raw_data[44:]

        print("KEY-->", key)
        f = Fernet(key)

        data = eval(f.decrypt(encrypted_data).decode())

        print("DATOS DESENCRIPTADOS -->", data)
        print("TYPE-->", type(data))

        password = data['token'].encode()

        f = Fernet(DECRIPTION_KEY)

        password = f.decrypt(password).decode()

        #posted_data = request.POST.dict()
        '''
        posted_data = request.POST.dict()


        fernet = Fernet(DECRIPTION_KEY)

        pass_encrypted =  posted_data['token'].encode()

        print("PASS ENCRYPTED->", pass_encrypted)
        password = fernet.decrypt(pass_encrypted).decode()
        print("PASSWORD->", password)
        '''


       #print("HACIENDO POST->", request.body)

        if password == UPLOAD_PASSWORD:
            print("CONTRASEÑA CORRECTA\n\n")

            unit = BusUnit.objects.get(id= data['id'])
            current_location = BusStop.objects.get(name= data['current_location'])
            unit.location = current_location
            unit.save()
        else:
            print("PASSWORD MALA -->", password)
    return http.JsonResponse(dato_prueba)