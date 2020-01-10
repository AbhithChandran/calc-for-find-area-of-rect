from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'acp1/home.html')
def index(request):
    return HttpResponse("django")
def about(request):
    return render(request,'static   /about.html')
