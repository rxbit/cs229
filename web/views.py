from django.shortcuts import render, render_to_response
from django.views import generic

# Create your views here.

def IndexView(request):
    return render_to_response('index.html')