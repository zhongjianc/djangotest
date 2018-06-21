

from django.http import HttpResponse,Http404
from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse('hello world')

def current_datetime(request):
    now = datetime.datetime.now()
    #t = get_template('current_datetime.html')
    #html = t.render({'current_date':locals()})
    #return HttpResponse(html)
    return render_to_response('current_datetime.html', {'current_date': now})

def hours_ahead(requesr,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html',{'hour_offset':offset,'next_time':dt})

