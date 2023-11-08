from django import forms
from crm.models import Employees
class EmployeesForm(forms.Form):
    name=forms.CharField()
    department=forms.CharField()
    salary=forms.IntegerField()
    email=forms.EmailField()
    contact=forms.CharField()
    age=forms.IntegerField()

class EmployesModelForm(forms.ModelForm):
    class Meta:
        model=Employees
        fields="__all__"