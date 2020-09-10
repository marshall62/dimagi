from django import forms

class UserForm(forms.Form):
    email = forms.EmailField()
    city = forms.CharField()
    state = forms.CharField(required=False)
    country = forms.CharField(required=False)


