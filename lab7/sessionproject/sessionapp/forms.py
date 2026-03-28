from django import forms

SUBJECTS = [
    ('Mathematics', 'Mathematics'),
    ('Physics', 'Physics'),
    ('Chemistry', 'Chemistry'),
    ('Computer Science', 'Computer Science'),
    ('Biology', 'Biology'),
]

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name', widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    roll = forms.CharField(max_length=20, label='Roll Number', widget=forms.TextInput(attrs={'placeholder': 'Enter roll number'}))
    subject = forms.ChoiceField(choices=SUBJECTS, label='Subject')