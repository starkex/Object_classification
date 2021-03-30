from django.shortcuts import render
from .forms import ImageUploadForm

def handle_uploaded_file(f):
   with open('img.jpg', 'wb+') as destination:
      for chunk in f.chunks():
         destination.write(chunk)

def home(request):
   return render(request,'home.html')

def imageprocess(request):
   form = ImageUploadForm(request.POST, request.FILES)
   if form.is_valid():
      handle_uploaded_file(request.FILES['image'])

   return render(request,'results.html')