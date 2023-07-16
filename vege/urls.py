from django.urls import path
from . import views

urlpatterns = [
 path('receipes/',views.receipes),
 path('delete_receipe/<id>/',views.delete_receipe,name='delete_receipe'),
 path('update_receipe/<id>/',views.update_receipes,name='update_receipe'),
 path('login_page/',views.login_page),
 path('register/',views.register),
 path('logout/',views.logout_page),
 path('Student/',views.get_students),
 path('see_marks/<student_id>/',views.see_marks , name = 'see_marks')

]

    


        
    
    