import django.shortcuts
from django.shortcuts import HttpResponse, render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    return render(request, "home.html")
