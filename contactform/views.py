from django.contrib.auth.models import User
from django.shortcuts import render

from django.http import HttpResponse
from .models.form import Contactform


# Create your views here.

def Contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        ins = Contactform( name = name, email=email, message=message)
        ins.save()

    return render(request, 'Cform.html')
