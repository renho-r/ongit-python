from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def index(req):
    context = {}
    return render(req, 'index.html', context)

def move(req):
    if req.is_ajax():
        action = req.POST.get('action')
        command = req.POST.get('command')
        print(action, command)
    return HttpResponse()