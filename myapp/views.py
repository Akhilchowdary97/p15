from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
def trail(request):
    return HttpResponse("<h1>Project is on Air</h1>")
def base(request):
    return render(request,"base.html")
def home(request):
    return render(request,"myapp/home.html")
def profile(request):
    name="Akhil"
    return render(request,"myapp/profile.html",{'name':name})
def get_demo(request):
    name=request.GET.get('name')
    return render(request,"get_demo.html",{'name':name})
def post_demo(request):
    if request.method=="POST": 
        name=request.POST.get('name')
        return HttpResponse("<h1>Thanks for submission MR./MS. {}</h1>".format(name))
    return render(request,"post_demo.html")
def register(request):
    if request.method=="POST":
        First_Name=request.POST.get("First_Name")
        Last_Name=request.POST.get("Last_Name")
        Email=request.POST.get("Email")
        Phone_Number=request.POST.get("Phone_Number")
        Password=request.POST.get("Password")
        date=request.POST.get("birthday_day")
        month=request.POST.get("birthday_month")
        year=request.POST.get("birthday_year")
        gender=request.POST.get("sex")
        if gender=="1":
            gender="FeMale"
        else:
            gender="Male"

        send_mail("Thanks For Registration","hello Mr./Ms.{} {}\n Thanks for Registering".format(First_Name,Last_Name),
        "m.akhilchowdary97@gmail.com",[Email,],fail_silently=False)
        return HttpResponse("{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br".format(First_Name,Last_Name,Email,Phone_Number,Password,gender,date,month,year))
    return render(request,"myapp/registration.html")