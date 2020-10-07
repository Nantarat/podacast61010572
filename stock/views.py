from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   # products = Product.objects.all()
    return render (request, 'frontend/index.html')
def contact(request):
    return render (request, 'frontend/contact.html')
def page2(request):
    return render (request, 'frontend/page2.html')
def page3(request):
    return render (request, 'frontend/page3.html')