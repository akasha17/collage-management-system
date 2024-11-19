from django.contrib import admin
from django.urls import path
from newapp import views

urlpatterns = [
    path('dep_add',views.dep_add,name='dep_add'),
    path('',views.index,name='index'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('teacherhome',views.teacherhome,name='teacherhome'),
    path('studenthome',views.studenthome,name='studenthome'),
    path('logins',views.logins,name='logins'),

    path('reg_teacher',views.reg_teacher,name='reg_teacher'),
    path('reg_student',views.reg_student,name='reg_student'),
    path('index',views.mainhome,name='mainhome'),
    path('viewstudents',views.viewstudents,name='viewstudents'),
    path('adminteacher',views.adminteacher,name='adminteacher'),
    path('approve/<int:aid>',views.approve,name='approve'),
    path('approved_stview',views.approved_stview,name='approved_stview'),
    # path('teview',views.teview,name='teview'),
    path('updates',views.updates,name='updates'),
    path('updatestudent/<int:uid>',views.updatestudent,name='updatestudent'),
    path('updateteacher/<int:uid>',views.updateteacher,name='updateteacher'),
    path('updatet',views.updatet,name='updatet'),
    path('lgout',views.lgout,name='lgout'),
    path('deletestud/<int:uid>',views.deletestud,name='deletestud'),
    path('deleteteach/<int:uid>',views.deleteteach,name='deleteteach'),
    path('depbystudent',views.depbystudent,name='depbystudent'),
     path('depbyteacher',views.depbyteacher,name='depbyteacher'),

    
    



]