from django.shortcuts import render, HttpResponse
from demoapp.models import Contact
from datetime import datetime
# Create your views here.

def index(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    data = []
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        textarea = request.POST.get("textarea")
        contact = Contact(name=name, email=email, textarea=textarea, date=datetime.today())
        contact.save()
    records = Contact.objects.all()
    return render(request, 'contact.html', {'records' : records})