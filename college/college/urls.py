"""college URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mycollege import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.index,name='index'),
    path('adhod',views.ad_hod,name='adhod'),
    path('loginpage',views.login_page,name='loginpage'),
    path('adminp',views.adminp,name='adminp'),
    path('student',views.student,name='student'),
    path('hod',views.hod,name='hod'),
    path('teacher',views.teacher,name='teacher'),
    path('adteacher',views.ad_teacher,name='adteacher'),
    path('adstudent',views.add_student,name='adstudent'),
    path('hoddata',views.add_hod_data,name='hoddata'),
    path('teacherdata',views.add_teacher_data,name='teacherdata'),
    path('studentdata',views.add_student_data,name='studentdata'),
    path('viewhod',views.view_hod,name='viewhod'),
    path('delhod/<int:hod_id>',views.delete_hod,name='delhod'),
    path('viewteacher',views.view_teacher,name='viewteacher'),
    path('delteacher/<int:t_id>',views.del_teacher,name='delteacher'),
    path('viewstudent',views.view_student,name='viewstudent'),
    path('delstudent/<int:st_id>',views.del_student,name='delstudent'),
    path('viewall',views.viewall,name='viewall'),
    path('adminstudentview',views.view_st_admin,name='adminstudentview'),
    path('deladminstudent/<int:st_id>',views.del_student_admin,name='deladminstudent'),
    path('deladminteacher/<int:teacher_id>',views.del_teacher_admin,name='deladminteacher'),
    path('approveteacher/<int:teacher_id>',views.approve_teacher,name='approveteacher'),
    path('approvestudent/<int:student_id>',views.approve_student,name='approvestudent'),
    path('login',views.login,name='login'),
    path('profile',views.profile,name='profile'),
    path('editprofilepage/<int:id>',views.profile_edit_page,name='editprofilepage'),
    path('<int:id>/editprofile',views.edit_profile,name='editprofile'),
    path('logout',views.logout_profile,name='logout'),
    path('leave',views.leave_page,name='leave'),
    path('applyleave',views.teacher_apply_leave,name='applyleave'),
    path('approvetleave/<int:user_id>',views.approve_teacher_leave,name='approvetleave'),
    path('teacherleave',views.teacher_leave_page,name='teacherleave'),
    path('hodleaveapproval',views.hod_leave_approval,name='hodleaveapproval'),
    path('hodapplyleave',views.hod_apply_leave,name='hodapplyleave'),
    path('hodleavepage',views.hod_leave_page,name='hodleavepage'),
    path('hodeleavehandler/<int:user_id>',views.hod_leave_approval_handler,name='hodleavehandler'),
    path('studentleavepage',views.student_leave_page,name='studentleavepage'),
    path('studentleavehandler',views.student_leave_handler,name='studentleavehandler'),
    path('studentleavapprove',views.student_leave_approve,name='studentleaveapprove'),
    path('studentleaveapprovehandler/<int:user_id>',views.student_leave_approve_handler,name='studentleaveapprovehandler'),
    path('delleave/<int:user_id>',views.del_leave,name='delleave'),
    path('hoddelleave/<int:user_id>',views.hod_del_leave,name='hoddelleave'),
    path('teacherdelleave/<int:user_id>',views.teacher_del_leave,name='teacherdelleave')


]
