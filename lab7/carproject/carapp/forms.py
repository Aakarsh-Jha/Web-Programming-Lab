from django import forms

MANUFACTURERS = [
    ('Toyota', 'Toyota'),
    ('Honda', 'Honda'),
    ('Ford', 'Ford'),
    ('BMW', 'BMW'),
    ('Mercedes', 'Mercedes'),
    ('Audi', 'Audi'),
    ('Hyundai', 'Hyundai'),
    ('Chevrolet', 'Chevrolet'),
]

class CarForm(forms.Form):
    manufacturer = forms.ChoiceField(choices=MANUFACTURERS, label='Car Manufacturer')
    model = forms.CharField(max_length=100, label='Model Name', widget=forms.TextInput(attrs={'placeholder': 'e.g. Camry, Civic, Mustang'}))