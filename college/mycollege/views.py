from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

from .models import Hod
from .models import Teacher
from .models import Student

# Create your views here.


def index(request):
    return render(request, 'index.html')


def ad_hod(request):
    return render(request, 'adhod.html')


def login(request):
    return render(request, 'login.html')


def adminp(request):
    return render(request, 'admin.html')


def student(request):
    return render(request, 'student.html')


def hod(request):
    return render(request, 'hod.html')


def teacher(request):
    return render(request, 'teacher.html')


def ad_teacher(request):
    return render(request, 'adteacher.html')


def add_student(request):
    return render(request, 'adstudent.html')




# add data to model hod

# hod data


def add_hod_data(request):

    if request.method == 'POST':
        first_name = request.POST['fname']
        second_name = request.POST['lname']
        user_name = request.POST['uname']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        department = request.POST['department']
        password = request.POST['password']
        password1 = request.POST['password1']
        qualification = request.POST['qualification']
        experience = request.POST['experience']

        status = '1'
        role = 'hod'

        if password == password1:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'Username taken')
                return redirect('adhod')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return redirect('adhod')

            else:
                user = User.objects.create_user(
                    username=user_name, password=password)
                user.save()

                data = Hod(user=user, first_name=first_name, second_name=second_name,
                           user_name=user_name, address=address,
                           email=email, phone=phone,
                           department=department, password=password, password1=password1, qualification=qualification,
                           experience=experience, status=status, role=role)
                data.save()

                print('hod added')

        else:
            messages.info(request, 'password is not matching')
            return redirect('adhod')

        return redirect('adminp')
    else:
        return render(request, 'adhod.html')


# teacher data
def add_teacher_data(request):

    if request.method == 'POST':
        first_name = request.POST['fname']
        second_name = request.POST['lname']
        user_name = request.POST['uname']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password1 = request.POST['password1']
        department = request.POST['department']
        subject = request.POST['subject']

        status = '0'
        role = 'teacher'

        if password == password1:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'username taken')
                return redirect('adteacher')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return redirect('adhod')
            else:
                user = User.objects.create_user(
                    username=user_name, password=password)
                user.save()

                data = Teacher(user=user,status=status, first_name=first_name,
                               second_name=second_name, user_name=user_name,
                               address=address, phone=phone, password=password,
                               password1=password1,
                               department=department, subject=subject)

                data.save()
        else:
            messages.info(request, 'password not matching')
            return redirect('adteacher')

        return redirect('hod')
    else:
        return render(request, 'adteacher.html')


# student data

def add_student_data(request):

    if request.method == 'POST':
        first_name = request.POST['fname']
        second_name = request.POST['lname']
        user_name = request.POST['uname']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password1 = request.POST['password1']
        department = request.POST['department']
        year = request.POST['year']

        status = '0'
        role = 'student'

        if password == password1:

            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'username exists')
                return redirect('adstudent')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email exists')
                return redirect('adstudent')
            else:
                user = User.objects.create_user(
                    username=user_name, password=password)
                user.save()

                data = Student(user=user,status=status, first_name=first_name, second_name=second_name,
                               user_name=user_name, address=address,
                               email=email, phone=phone,
                               department=department, year=year, password=password, password1=password1)

                data.save()

        else:
            messages.info(request, 'password not matching')
            return redirect('adstudent')

        return redirect('teacher')
    else:
        return redirect(request, 'adstudent.html')






# view hod data

def view_hod(request):
    hod_data = Hod.objects.all()
    return render(request, 'viewhod.html', {'data': hod_data})


# delete hod data

def delete_hod(request, hod_id):
    hod_data = Hod.objects.get(id=hod_id)
    hod_data.delete()
    return redirect('viewhod')


# view teachers

def view_teacher(request):
    t_data = Teacher.objects.all()
    return render(request, 'viewteacher.html', {'data': t_data})


# delete teacher

def del_teacher(request, t_id):
    del_data = Teacher.objects.get(id=t_id)
    del_data.delete()
    return redirect('viewteacher')


# view student

def view_student(request):
    student_data = Student.objects.all()
    return render(request, 'viewstudent.html', {'data': student_data})


# delete student

def del_student(request, st_id):
    del_data = Student.objects.get(id=st_id)
    del_data.delete()
    return redirect('viewstudent')

#view teachers and students

def viewall (request):
    all_data=Teacher.objects.all()

    return render(request,'viewall.html',{'data':all_data})


def view_st_admin(request):
    data=Student.objects.all()
    return render (request,'adminstudentview.html',{'data':data})

#delete admin view student
def del_student_admin(request, st_id):
    del_data = Student.objects.get(id=st_id)
    del_data.delete()
    return redirect('adminstudentview')

#delete teacher view student

def del_teacher_admin(request,teacher_id):
    del_data=Teacher.objects.get(id=teacher_id)
    del_data.delete()
    return redirect("viewall")


#approve teacher

def  approve_teacher(request,teacher_id):
    teacher=Teacher.objects.get(id=teacher_id)
    teacher.status='1'
    teacher.save()
    return redirect('viewall')


#approve students


def approve_student(request,student_id):
    student=Student.objects.get(id=student_id)
    student.status='1'
    student.save()
    return redirect("adminstudentview")





#login

stat=''
rol=''

def login(request):
    global status
    global role

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(username=username,password=password)

        data=User.objects.filter(username=username).values()
        
        for i in data:
            user_name=i['username']

            i=i['id']


            ds=Student.objects.filter(user_id=id).values()

            for i in ds:
                stat=i['status']
                rol=i['role']


            dt=Teacher.objects.filter(user_id=id).values()
            
            for i in dt:
                stat=i['status']
                rol=i['role']


            dh=Hod.objects.filter(user_id=id).values()

            for i in dh:
                stat=i['status']
                rol=i['role']


            if user is not None and rol=='student' and username==user_name and stat=='1':
                auth_login(request,user)
                return redirect('student')

            elif user is not None and rol=='teacher'  and username==user_name and stat=='1':
                auth_login(request,user)
                return redirect('teacher')

            elif user is not None and rol=='hod' and username==user_name and stat=='1':
                auth_login(request,user)
                return redirect('hod')
            
            elif username=='admin' and password =='admin123':
                auth_login(request,user)
                return redirect('adminp')

            else:
                pass
        else:
            messages.info(request,'invalid credential')
            return redirect('login')

    else:
        return render(request,'login.html')    

        


