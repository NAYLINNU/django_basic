from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employee

def home(request):
    # return HttpResponse('hello world')
    
    employees = Employee.objects.all()  #take care this systnax dose not contain .get() function
    context = {
        'employees':employees,
    }
    return render(request,'home.html', context)