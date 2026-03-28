from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model  = Student
        fields = ['student_id', 'name', 'course_name', 'dob']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }