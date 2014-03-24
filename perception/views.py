from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.template.loader import render_to_string

# Create your views here.
from perception.models import *

def motion_result(request, camera=1):
    point_list = Motion.objects.filter(camera__id=camera)
    point_list = point_list.filter(added__range=["2014-03-03", "2011-03-10"])
    return render_to_response('camera_result.html', {
        'point_list': point_list,
        'camera': camera
    }, context_instance=RequestContext(request))