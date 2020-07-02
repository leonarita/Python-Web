from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {}, cuja idade é {} anos!</h1>'.format(nome, idade))
