from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q,Sum
from .admin import total_marks
from .seed import generate_report_card
# from django.contrib.auth import get_user_model

# User = get_user_model()
# Create your views here.


@login_required(login_url="/vege/login_page/") # mtlb receipes ka page kholne se phele login page kholo aur vaaha login krke aao
def receipes(request):

    if request.method == "POST": # yeh frontend se backend mae jaana ho toh
        data = request.POST
        # receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_desc = data.get('receipe_desc')
        print(receipe_name)
        print(receipe_desc)
        # print(receipe_image)

# CRUD OPERATION:     C:create ,  R:read ,  U:update  ,  D:delete

# CREATE OPEARTION
#M1)  receipe.object.create(receipe_name="pasta",receipe_desc="pasta is a very good dish")
#M2)        
        receipe.objects.create(
        receipe_name = receipe_name,
        receipe_desc = receipe_desc,
        #  receipe_image = receipe_image
       )
    # return redirect('/receipes/')

# READ OPEARTION
    queryset = receipe.objects.all() 
    #Read krane ka tareeka
    #receipe.objects.get(id = 1)     agr ek specific ko krana ho toh
    context = {'receipes':queryset}
    return render(request,'receipes.html', context)

# DELETE OPERATION
def delete_receipe(request, id):
    queryset = receipe.objects.get(id = id)
    # print(queryset)
    queryset.delete()
    return redirect('/vege/receipes/')

# UPDATE OPEARTIOn
def update_receipes(request, id):
    queryset = receipe.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        # receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get("receipe_name")
        receipe_desc = data.get("receipe_desc")

        queryset.receipe_name = receipe_name
        queryset.receipe_desc = receipe_desc
        # queryset.receipe_image = receipe_image
          
        queryset.save()
        return redirect('/vege/receipes/')
    context = {'update_receipes':queryset}
    return render(request,'update_receipes.html', context)
   
    # return redirect('/receipes/')
def login_page(request):
    
    print(request.method)
    if request.method == "GET":
       

        Username = request.POST.get('Username')
        Password = request.POST.get('Password')

        print("\n\n\n\n\n\n\n\n",Username,Password,"\n\n\n\n\n\n\n\n\n")

        user= User.objects.filter(username = Username)
        if user.exists():
            messages.error(request,'Invalid user')
            return redirect('/vege/login_page/') 
            # return redirect('/login/') 

        user = authenticate(username = Username , password = Password)

        if user is None:
            messages.error(request,'Invalid password')

            return redirect('/vege/login_page/')    

        else:
            login(request,user=user)  
            return redirect('/vege/receipes/')
    return render(request ,'login.html')


# https://github.com/AseemGupta39/django_newton/

def logout_page(request):
    logout(request)
    return redirect('/vege/login_page/')
   

def register(request):
    print("\n\n\n\n\n\n\n\n","chal if ke upar ahi","\n\n\n\n\n\n\n\n\n")

    print(request.method)

    if request.method == "POST":
        First_name = request.POST.get('First_name')
        Last_name = request.POST.get('Last_name')
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')

        user = User.objects.filter(username=Username)
        if user.exists():
           messages.error(request,'Invalid user')
           
           return redirect('/vege/login_page/') 

        user = User.objects.create(
               first_name=First_name,
               last_name=Last_name,
               username=Username)
        
        user.set_password(Password)
        user.save()
        messages.success(request,'Account created successfully')
        return redirect('/vege/register/') 

    return render(request,'D:\\prac_mysql\\core\\core\\vege\\templates\\register.html')



def get_students(request):
    queryset = Student.objects.all()
    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks','-student_age')
    if request.GET.get('search'):
       search = request.GET.get('search')
       queryset = queryset.filter(
    Q(student_name__icontains = search) |
    Q(department__department__icontains = search) |
    Q(student_id__student_id__icontains = search)|
    Q(student_name__icontains = search)|
    Q(student_email__icontains = search)
)
    return render(request , 'report/students.html',{'queryset':queryset})





def see_marks(request , student_id):
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    return render(request , 'report/see_marks.html',{'queryset':queryset , 'total_marks': total_marks })



















## from django.contrib.auth.models import User
## User.objects.all()