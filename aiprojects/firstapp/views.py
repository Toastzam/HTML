from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hi(request):
    return HttpResponse("<h1>hello Django</h1>")
def carami(request):
    return HttpResponse("<h1>성공</h1>")
def young(request):
    return HttpResponse("<h1>여기는</h1><ul>감귤은 맛있습니다.</ul><h2>청취다방입니다.</h2>")