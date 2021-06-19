""" Posts views. """
#from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def list_posts(request):
    """ List existing posts"""
    posts = [1,2,4]
    return HttpResponse(str(posts))