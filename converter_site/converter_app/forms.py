from django import forms

class UTFForm(forms.Form):
    utf_input = forms.CharField(label='Your input', max_length=1000)