from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to NFuture Admin Page!")

urlpatterns = [
    path('', home),
]