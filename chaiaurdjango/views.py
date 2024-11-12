from django.http import HttpResponse
from django.shortcuts import render
from chai.models import ChaiVariety  # Import ChaiVariety from the chai app

def home(request):
    chai_varieties = ChaiVariety.objects.all()  # Fetch all chai varieties
    return render(request, "websites/index.html", {"chai_varieties": chai_varieties})

def about(request):
    return HttpResponse("Hello World. You are at Chai aur django About Page")

def contact(request):
    return HttpResponse("Hello World. You are at Chai aur django Contact Page")
