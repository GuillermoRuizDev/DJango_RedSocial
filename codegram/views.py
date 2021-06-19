""" CodeGram URLs views """

import json
from django.http import HttpResponse,JsonResponse


# Utilities
from datetime import date, datetime

def hello_world(request):    
    return HttpResponse('Oh, hi Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def sorted_integers(request):
    # Function for sort integers
    #import pdb; pdb.set_trace()
    numbers = [int(i) for i in request.GET['number'].split(',')]
    numbers.sort()
    data = {
        'status': 'ok',
        'number': numbers,
        'message': 'Integers sorted successfully.'
    }
    #return JsonResponse(data, safe=False) #Funciona bien en caso de solo enviar json
    return HttpResponse(json.dumps(data, indent=3), content_type='application/json')

def say_hi(request, name, age):
    #Return a greeting
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}!, welcome to CodeGram'.format(name)
    return HttpResponse(message)
        