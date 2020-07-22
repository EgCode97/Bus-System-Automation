from django.shortcuts import render
import django.http as http
from django.views.decorators.csrf import csrf_exempt

from .models import BusStop, BusUnit, Route, Zone, Register
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

        if password == UPLOAD_PASSWORD:
            print("CONTRASEÑA CORRECTA\n\n")

            unit = BusUnit.objects.get(id=data['id'])
            current_location = BusStop.objects.get(name=data['current_location'])
            unit.location = current_location
            unit.save()

            # register the bus stop in register table
            reg = Register(location=current_location, unit= unit, datetime= data['time'])
            reg.save()
            print(reg)
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

    return render(request, "home.html", context=context)


def busqueda(request, query_param):
    context = dict()
    context['title'] = "Buscar"

    context['style_search'] = True

    if query_param == 'rutas':
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


def ver(request, query_object, query_param):
    context = dict()

    if query_object == 'ruta':
        context['title'] = f"Ruta {query_param}"
        context['style_route_path'] = True

        # Get the units asignated to the given route
        context['units'] = BusUnit.objects.filter(route__name__iexact= query_param)
        print(context['units'])


        # get the bus stops for the given route
        route_stops = Route.objects.get(name=query_param).get_route_stops()
        print(route_stops)
        print(type(route_stops))
        context['route_stops'] = enumerate(route_stops)

        return render(request, 'route_path.html', context)


    elif query_object == 'zona':
        # get the bus stops from the given zone
        zone_stops = BusStop.objects.filter(zone__name__iexact= query_param)
        print(query_param)
        print(zone_stops)
        context['content_type'] = 'bus_stops'
        context['style_search'] = True
        context['stops'] = zone_stops

        return render(request, "search.html", context)

    elif query_object == 'parada':
        context['title'] = 'Parada %s' %(query_param)
        context['style_stop_register'] = True

        routes = list()
        existing_routes = Route.objects.all() #get all the Routes created
        for route in existing_routes:
            print(route.get_route_stops())
            for stop in route.get_route_stops():
                print(stop.name, type(stop.name))
                if stop.name == query_param:
                    print("ES IGUAL")
                    routes.append(route)
                    break
        context['routes'] = routes
        print("LAS RUTAS SON", context['routes'])
        return render(request, "stop_info.html", context)
