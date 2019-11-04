from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse


def hello(request):
    # return HttpResponse("Hello world ! ")
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

def rebaidu(request):
    return redirect('http://www.baidu.com')
    # return  redirect('/hello')