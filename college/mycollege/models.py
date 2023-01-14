from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#model for hod
class Hod(models.Model):


    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=200)
    second_name=models.CharField(max_length=200)
    user_name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.IntegerField()
    department=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    password1=models.CharField(max_length=200)
    qualification=models.CharField(max_length=200)
    experience=models.IntegerField()
    status=models.CharField(max_length=200)
    role=models.CharField(max_length=200)

    def __str__(self):
        return self.first_name

#model for teacher

class Teacher(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=200)
    second_name=models.CharField(max_length=200)
    user_name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.IntegerField()
    department=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    password1=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    role=models.CharField(max_length=200)
    

    def __str__(self):
        return self.first_name

#model for student

class Student(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=200)
    second_name=models.CharField(max_length=200)
    user_name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.IntegerField()
    department=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    password1=models.CharField(max_length=200)
    year=models.IntegerField()
    status=models.CharField(max_length=200)
    role=models.CharField(max_length=200)

    

    def __str__(self):
        return self.first_name

#model  for leave approval

class Approval(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    department=models.CharField(max_length=200)
    reason=models.CharField(max_length=500)
    status=models.CharField(max_length=50)
    role=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
     

    
