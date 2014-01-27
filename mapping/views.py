from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404, redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext

def front_page(request):
    return render_to_response('front.html', {}, context_instance=RequestContext(request))