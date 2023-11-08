from django.shortcuts import render,redirect

# Create your views here.
from crm.forms import EmployeesForm,EmployesModelForm
from django.views.generic import View
from crm.models import Employees

class EmployecreateView(View):
    def get(self,request,*args,**kwargs):
         form=EmployesModelForm()
         return render(request,"emp_add.html",{"form":form})
    def post(self,request,*args,**kwargs):
         form=EmployesModelForm(request.POST)
         if form.is_valid():
              form.save()
          #     Employees.objects.create(**form.cleaned_data)
              print("created")
              return render(request,"emp_add.html",{"form":form})
         else:
              return render(request,"emp_add.html",{"form":form})
         
class EmployelistView(View):
     def get(self,request,*args,**kwargs):    
          qs=Employees.objects.all()
          return render(request,"emp_list.html",{"data":qs})
     

class EmployedetailView(View):
     def get(self,request,*args,**kwargs):
          id=kwargs.get("pk")
          qs=Employees.objects.get(id=id)
          return render(request,"emp_detail.html",{"data":qs})
     

class EmployeDeleteView(View):
     def get(self,request,*args,**kwargs):
           id=kwargs.get("pk")
           Employees.objects.get(id=id).delete()
           return redirect ("emp-all")
     