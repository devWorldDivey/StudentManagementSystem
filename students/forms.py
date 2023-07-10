from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number','first_name','last_name','email','field_ofstudy','gpa']
        labels = {
            'student_number':'Student Number',
            'first_name':'First Name',
            'last_name' : 'Last Name',
            'email': 'Email',
            'field_ofstudy' : 'Field of Study',
            'gpa':'GPA'
        }
        widgets = {
            'student_number':forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'field_ofstudy' : forms.TextInput(attrs={'class': 'form-control'}),
            'gpa':forms.NumberInput(attrs={'class': 'form-control'}),
        }