from django import forms
from django.contrib.auth.forms import UserCreationForm
from classroom.models import User,Manager,Employee,Adminn,Leave
from django.db import transaction
import datetime

## User Login Form (Applied in both student and teacher login)
class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username','password1','password2']
        widgets = {
                'username': forms.TextInput(attrs={'class':'answer'}),
                'password1': forms.PasswordInput(attrs={'class':'answer'}),
                'password2': forms.PasswordInput(attrs={'class':'answer'}),
                }
        
## Teacher Registration Form 
class ManagerProfileForm(forms.ModelForm):
    class Meta():
        model =  Manager
        fields = ['name','dept_name','phone','email']
    
        widgets = {
                'name': forms.TextInput(attrs={'class':'answer'}),
                'dept_name': forms.TextInput(attrs={'class':'answer'}),
                
                'phone': forms.NumberInput(attrs={'class':'answer'}),
                'email': forms.EmailInput(attrs={'class':'answer'}),
                }

## Teacher Profile Update Form
class AdminProfileUpdateForm(forms.ModelForm):
    class Meta():
        model = Adminn
        fields = ['name','email','phone']
class AdminProfileForm(forms.ModelForm):
    class Meta():
        model =  Adminn
        fields = ['name','phone','email']
        widgets = {
                'name': forms.TextInput(attrs={'class':'answer'}),
                'phone': forms.NumberInput(attrs={'class':'answer'}),
                'email': forms.EmailInput(attrs={'class':'answer'}),
                }

## Teacher Profile Update Form
class ManagerProfileUpdateForm(forms.ModelForm):
    class Meta():
        model = Manager
        fields = ['name','dept_name','email','phone']

## Student Registration Form
class EmployeeProfileForm(forms.ModelForm):
    class Meta():
        model =  Employee
        fields = ['name','dept_name','phone','email']
        
        widgets = {
                'name': forms.TextInput(attrs={'class':'answer'}),
                'dept_name': forms.TextInput(attrs={'class':'answer'}),
                'phone': forms.NumberInput(attrs={'class':'answer'}),
                'email': forms.EmailInput(attrs={'class':'answer'}),
                }

## Student profile update form
class EmployeeProfileUpdateForm(forms.ModelForm):
    class Meta():
        model = Employee
        fields = ['name','dept_name','email','phone']



class LeaveCreationForm(forms.ModelForm):
    class Meta():
        model =  Leave
        fields = ['startdate','enddate','leavetype','reason']
        
        widgets = {
            'startdate': forms.DateInput(attrs={'type': 'date'}),
            'enddate': forms.DateInput(attrs={'type': 'date'}),
                }

    
    



    