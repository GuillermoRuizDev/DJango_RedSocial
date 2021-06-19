"""" CodeGram Urls module """

from django.urls import path
from codegram import views



urlpatterns = [
    #path('admin/', admin.site.urls),
    path('hello-world/', views.hello_world),
    path('sorted_integers/', views.sorted_integers),
    path('hi/<str:name>/<int:age>/', views.say_hi)
]
