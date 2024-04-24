# from django.http import HttpResponse;
from django.shortcuts import render

def homepage(request):
  # return HttpResponse("This is home page")
  return render(request, "home.html")

def aboutpage(request):
  # return HttpResponse("This is about page")
  return render(request, "about.html")