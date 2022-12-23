from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'index.html')


def registration(request):
    return render(request,'registration.html')


def login(request):
    return render(request,'login.html')


def adminp(request):
    return render (request,'admin.html')


def student(request):
    return render(request,'student.html')

    
def hod(request):
    return render(request,'hod.html')


def teacher(request):
    return render(request,'teacher.html')




