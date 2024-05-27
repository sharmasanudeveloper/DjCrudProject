from django.shortcuts import render,redirect
from django.http import HttpResponse
from crudapp.models import Student

# Create your views here.
# FOr Home Page
def home(request):
    std = Student.objects.all()
    return render(request,'index.html',{'stdnt':std})


# For Add student Detail In Form
def addstudent(request):
    if (request.method == 'POST'):
        
        name=request.POST.get('stdnm')
        age=request.POST.get('stdag')
        email=request.POST.get('stdmail')
        address=request.POST.get('stdadrs')
        department=request.POST.get('stddpr')
        print(name,age,email,address,department)
        
        st = Student(name=name,age=age,email=email,address=address,department=department)
        st.save()
        
        print('data extract')
        return redirect('/registration/')
    return render(request,'addstudent.html')


# For Delete student Detail In Form
def delete(request,id):
    dt = Student.objects.get(id=id)
    dt.delete()
    print('Delete')
    return redirect('/registration/')


# For Any Updation In Student Data
def updat(request,id):
    up = Student.objects.get(id=id)
    if (request.method == 'POST'):   
        up.name=request.POST.get('stdnm')
        up.age=request.POST.get('stdag')
        up.email=request.POST.get('stdmail')
        up.address=request.POST.get('stdadrs')
        up.department=request.POST.get('stddpr')
        up.save()
        return redirect('/registration/')
    return render(request,'update.html',{'update':up})
    