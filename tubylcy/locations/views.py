from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template('locations/index.html')
    context = RequestContext(request, {
        #here shit from *models* useful for webpage
    })
    return HttpResponse(template.render(context))

