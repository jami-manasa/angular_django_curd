from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from app.models import Employee
from app.forms import EmployeeForm



# Create your views here.
def show_view(request):
    employees=Employee.objects.all()
    return render(request,'app/index.html',{'employees':employees})
def create_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'app/create.html',{'form':form, 'res':'true', 'msg':'Added', 'classStyle':"alert "})
        else:
            return render(request,'app/create.html',{'form':form, 'res':'true', 'msg':'Invalid', 'classStyle':"alert "})
    else:
        return render(request,'app/create.html',{'form':form})
def delete_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    employees=Employee.objects.all()
    return render(request,'app/index.html',{'employees':employees, 'res':'true', 'msg':'Deleted ', 'classStyle':"alert "})
def update_view(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST ,instance=employee)
        if form.is_valid():
            form.save()
            return render(request,'app/update.html',{'employee':employee,'res':'true','msg':' Updated ', 'classStyle':"alert alert-dark"})
        else:
            return render(request,'app/update.html',{'employee':employee,'res':'false', 'msg':'Invalid', 'classStyle':'alert alert-dark'})
    else:
        return render(request,'app/update.html',{'employee':employee,'res':'false'})
