from django.shortcuts import render
from django.http import HttpResponse 
from django.template.loader import get_template
from django.shortcuts import render_to_response
from books.models import Book
import datetime
# Create your views here.

def index(request):
    return HttpResponse('hello world')

def test(request):
    now = datetime.datetime.now()
    #t = get_template('current_datetime.html')
    #html = t.render({'current_date':locals()})
    #return HttpResponse(html)
    return render_to_response('current_datetime.html', {'current_date': now})

def search_form(request):
    return render_to_response('search_form.html')

'''
def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)'''

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        #books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_results.html',
            {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')