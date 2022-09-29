from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Employee

# Create your views here.

def openIndexPage(request):
    return render(request,"index.html")

def openEmployeeForm(request):
    return render(request,"employee-form.html")

def saveEmployee(request):
    employee=Employee()
    employee.name=request.POST['name']
    employee.phone=request.POST['phone']
    employee.salary=request.POST['salary']
    employee.dob=request.POST['dob']
    employee.save()
    return redirect("/employees-list")

def getAllEmployees(request):
    employees=Employee.objects.all()
    return render(request,"employees-list.html",{'employees':employees})

def removeEmployee(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect("/employees-list")

def editEmployee(request,id):
    employee=Employee.objects.get(id=id)
    return render(request,"employee-update-form.html",{'employee':employee})

def updateEmployee(request,id):
    employee=Employee.objects.get(id=id)
    employee.name=request.POST['name']
    employee.phone=request.POST['phone']
    employee.salary=request.POST['salary']
    employee.dob=request.POST['dob']
    employee.save()
    return redirect("/employees-list")