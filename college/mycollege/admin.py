from django.contrib import admin
from .models import Hod
from .models import Teacher
from .models import Student,Approval

# Register your models here.
admin.site.register(Hod)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Approval)

