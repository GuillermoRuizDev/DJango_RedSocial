""" Posts views. """

from django.shortcuts import render
# Create your views here.
from datetime import datetime
posts = [
    {
        'name':'Mont Blac',
        'user':'Yesica Cortés',
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036'
    },

    {
        'name': 'Via Láctea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903',
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'Thespianartist',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076',    
        }    
]

def list_posts(request):
    """ List existing posts"""
    return render(request,'feed.html')