from django.shortcuts import render

def home(request):
   return render(request,'home.html')

def imageprocess(request):
   return render(request,'results.html')