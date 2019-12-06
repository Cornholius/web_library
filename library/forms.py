from django import forms


class UserForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))


class UserForm2(forms.Form):
    name2 = forms.CharField()