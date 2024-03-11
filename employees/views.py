from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from employees.models import Employee

# Create your views here.


def employee_detail(request,pk):
    
    # try:                             ### That is print will value in console not in browser
    #     employee=Employee.objects.get(pk=pk)
    #     print(employee)
    # except:
    #     raise Http404
    
    
     
   # employee = get_object_or_404(Employee,pk=pk)
    # print(employee)           ### That is print will value in console not in browser
    
    #return HttpResponse(employee)  ##That is show data in broswer
    
    employee = get_object_or_404(Employee,pk=pk)
    
    context = {
        'employee':employee,
    }
    return render(request,'employee_detail.html',context)