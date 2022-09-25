from django.shortcuts import render,HttpResponse      #render is use to render the templates
from datetime import datetime
from Home.models import Contact
# Create your views here.
def index(request):
    
    return render(request,'index.html',{'name':'navin'})
                                                       #This process of urls is called as url dispatchinng # Internship(urls.py) -> Home(urls.py) it will check if path is mmatching then -> views(functions) 
def about(request):
    return render(request,'about.html',)    

def news(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
    
    return render(request,'news.html',)      
 

def contact(request):
    return render(request,'contact.html',)   

     