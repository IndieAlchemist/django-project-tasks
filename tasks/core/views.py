from django.shortcuts import render
from django.http import HttpResponse

import datetime
import random

from .utils import do_request

# Create your views here.


def test_view(request):
    html = "<html><body><h1>Hello World!!!</h1></body></html>"
    r=do_request('http://localhost:8000/time/')
    if r.status_code == 200:
        return HttpResponse(r.text)
    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    
    entropy=random.randint(1,10)
        
    if entropy>7:
        return HttpResponse(html)

    return HttpResponse(status=408)
