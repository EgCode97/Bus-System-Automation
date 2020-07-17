from django.shortcuts import render
import django.http as http
from django.views.decorators.csrf import csrf_exempt

from .models import BusStop, BusUnit, Route, Zone
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


def home(request):
    context = dict()
    context['title'] = "Home"

    context['style_home'] = True

    context['stops'] = [stop.name for stop in BusStop.objects.all()]
    context['routes'] = [route.name for route in Route.objects.all()]
    context['zones'] = [zone.name for zone in Zone.objects.all()]

    print(context)
    return render(request, "home.html", context=context)


def busqueda(request, query_param):
    context = dict()
    context['title'] = "Buscar"

    context['style_search'] = True

    if query_param=='rutas':
        context['content_type'] = 'routes'
        context['title'] += " Rutas"
        context['routes'] = [route for route in Route.objects.all()]

    elif query_param == 'paradas':
        context['content_type'] = 'bus_stops'
        context['title'] += " Paradas"
        context['stops'] = [stop for stop in BusStop.objects.all()]
    
    else:
        context['content_type'] = 'zones'
        context['title'] += " Zonas"
        context['zones'] = [zone for zone in Zone.objects.all()]

    return render(request, "search.html", context)