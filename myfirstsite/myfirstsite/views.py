#created by own
from django.db.models.fields import return_None
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    param={"name":"Jhone","language":"english"}
    return render(request,'index.html',param)

def about(request):
    param={"name":"Nitesh","language":"python"}
    # return HttpResponse("hello this is about ")
    return render(request,'index.html',param)

def removepunc(request):
    return HttpResponse("you are inside the removepunc function")

def capitalizestring(request):
    return HttpResponse("you are inside the capitalizestring function")

def newlineremover(request):
    return HttpResponse("you are inside the newlineremover function")

def spaceremover(request):
    return HttpResponse("you are inside the spaceremover function")

def countchar(request):
    return HttpResponse("you are inside the charcount function")
