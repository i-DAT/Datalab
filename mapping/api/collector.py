from mapping.models import *

from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response

from django.views.decorators.csrf import csrf_exempt

from tastypie.models import ApiKey

import json

import paho.mqtt.client as paho
from settings import broker


#custom method for collecting gps data
@csrf_exempt
def collect_location(request):
    success = False
    
    #check for a key
    if request.GET.get("api_key"):

        try:
            key = ApiKey.objects.get(key=request.GET.get('api_key'))

            if request.method == "POST":
                data = json.loads(request.body)

                the_device, created = Device.objects.get_or_create(
                    serial=data['serial']
                )

                the_location = Location()
                the_location.device = the_device
                the_location.lat = data['lat']
                the_location.long = data['long']
                the_location.activity = data['activity']
                the_location.confidence = data['confidence']

                the_location.save()

                success = True

        except ApiKey.DoesNotExist:
            success = "Error - ApiKey DoesNotExist"

    return render_to_response('success.json', {
        'success': success,
    }, context_instance=RequestContext(request))


def collect_get_location(request):
    success = False
    
    #check for a key
    print request.GET
    if request.GET.get("api_key"):

        key = ApiKey.objects.get(key=request.GET.get('api_key'))

        the_device, created = Device.objects.get_or_create(
            serial=request.GET.get('serial')
        )

        the_location = Location()
        the_location.device = the_device
        the_location.lat = request.GET.get('lat')
        the_location.long = request.GET.get('long')
        the_location.activity = request.GET.get('act')
        the_location.confidence = request.GET.get('conf')

        the_location.save()

        success = True

    return render_to_response('success.json', {
        'success': success,
    }, context_instance=RequestContext(request))


def collect_comment(request):
    success = False
    
    #check for a key
    print request.GET
    if request.GET.get("api_key"):

        key = ApiKey.objects.get(key=request.GET.get('api_key'))

        if request.GET.get("api_key"):

            the_device, created = Device.objects.get_or_create(
                serial=request.GET.get('serial')
            )

            the_comment = Comment()
            the_comment.device = the_device
            the_comment.text = request.GET.get('com')

            the_comment.save()

            success = True

    return render_to_response('success.json', {
        'success': success,
    }, context_instance=RequestContext(request))


def collect_imp_data(request):
    success = False
    
    #check for a key
    print request.GET
    if request.GET.get("api_key"):

        #key = ApiKey.objects.get(key=request.GET.get('api_key'))

        #the_imp, created = Imp.objects.get_or_create(
        #    serial=request.GET.get('serial')
        #)

        #the_sensor = Sensor.objects.get(
        #    shortcode = request.GET.get('sensor')
        #)

        #the_reading = Reading()
        #the_reading.imp = the_imp
        #the_reading.sensor = the_sensor
        #the_reading.amount = request.GET.get('value')

        #the_reading.save()

        #success = True

        client = paho.Client(broker.CLIENT_ID)
        client.connect(broker.ADDRESS, broker.MQTT_PORT)
        client.publish("datalab/imp/" + request.GET.get('serial') + "/" + request.GET.get('sensor'), request.GET.get('value'), 1)
        client.disconnect()

    return render_to_response('success.json', {
        'success': success,
    }, context_instance=RequestContext(request))