from mapping.models import *

from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response

from django.views.decorators.csrf import csrf_exempt

from tastypie.models import ApiKey

import json


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
