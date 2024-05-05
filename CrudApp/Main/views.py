from django.shortcuts import render , redirect
from . models import reminder

# Create your views here.

def index(request):
    rem = reminder.objects.all()
    dec_data = {"rem":rem}
    return render(request,"index.html",dec_data)

def Insertdata(request):
    return render(request,"Insert_data.html")

def register(request):
    if request.method == "POST":
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        date = request.POST.get('date')
        data = reminder(title=title,desc=desc,date=date)
        data.save()
        return redirect('index')
    return render(request,'register')

def deldata(request,title):
    data = reminder.objects.get(title=title)
    data.delete()
    return redirect('index')

def viewdata(request,title):
    data = reminder.objects.get(title=title)
    dec_data = {"data":data}
    return render(request,"viewdata.html",dec_data)

def updatedata(request):
    if request.method == "POST":
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        date = request.POST.get('date')
        
        reminder.objects.filter(title=title).update(title=title,desc=desc,date=date)
        return redirect('index')

