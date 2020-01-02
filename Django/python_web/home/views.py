from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    response = HttpResponse()
    response.writelines('<h1>Hello there</h1>')
    response.write('I am the LA Beast!')
    return response
