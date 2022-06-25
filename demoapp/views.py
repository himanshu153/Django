from django.shortcuts import render, HttpResponse
from demoapp.models import Contact, users
from datetime import datetime
# Create your views here.

def index(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        records = users.objects.all()
        for record in records:
            if email == record.email and password == record.password:
                return HttpResponse("Logged in successfully")
            else:
                return HttpResponse("Invalid username or password")
        
    return render(request, 'user/login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = users(name=name, email=email, password=password)
        user.save()
    return render(request, 'user/register.html')

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