from re import template
from django.shortcuts import render

# Create your views here.

def Hello(request):
    template="index.html"
    context={}
    return render(request, template, context)