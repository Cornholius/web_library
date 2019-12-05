from django import forms


class UserForm(forms.Form):
    name = forms.CharField()


class UserForm2(forms.Form):
    name2 = forms.CharField()