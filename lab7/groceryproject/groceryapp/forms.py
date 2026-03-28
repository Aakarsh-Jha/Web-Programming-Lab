from django import forms

GROCERY_ITEMS = [
    ('Wheat', 'Wheat'),
    ('Jaggery', 'Jaggery'),
    ('Dal', 'Dal'),
    ('Rice', 'Rice'),
    ('Sugar', 'Sugar'),
    ('Salt', 'Salt'),
]

class GroceryForm(forms.Form):
    items = forms.MultipleChoiceField(
        choices=GROCERY_ITEMS,
        widget=forms.CheckboxSelectMultiple,
        label='Select Item'
    )