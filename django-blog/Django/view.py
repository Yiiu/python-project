from django.http import HttpResponse

def home (req):
    return HttpResponse('hello world')

def blog (req):
    return HttpResponse('hello Blog')