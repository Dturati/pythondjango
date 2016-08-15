from django.shortcuts import render
from django.http import HttpResponse

#Minha view home
#toda view recebe um request
def home(request):
    return render(request,'home.html',{'usuario':'David S. Turati'})

def contact(request):
    return render(request,'contact.html',{})

# Create your views here.
