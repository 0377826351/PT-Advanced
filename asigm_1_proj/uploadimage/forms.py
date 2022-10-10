from django import forms

class AnimalForm(forms.Form):
    name = forms.CharField(max_length=255)
    age = forms.IntegerField()
    color = forms.CharField(max_length=255)