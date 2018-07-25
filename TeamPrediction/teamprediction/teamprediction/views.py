from django.http import HttpResponse
from django.http import Http404
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_time(request):
    now = datetime.datetime.now()
    html = "<html><h3>First Dynamic Program</h3><body>It is now %s.</body></html>" % now        
    return HttpResponse(html)

#URLconfs and Loose Coupling
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>Currently it is %s and in %s hour(s),'\n' it will be  %s.</body></html>" % (datetime.datetime.now(), offset, dt)
    return HttpResponse(html)