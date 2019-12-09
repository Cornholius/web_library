from django import forms


class UserForm(forms.Form):

    search_field = forms.CharField(label='', widget=forms.TextInput(attrs={'size': '40'}))


class AddBookForm(forms.Form):

    author = forms.CharField(label='Автор', max_length=120, widget=forms.TextInput(attrs={'size': '68'}))
    book_name = forms.CharField(label='Название', max_length=120, widget=forms.TextInput(attrs={'size': '68'}))
    description = forms.CharField(required=False, label='Описание',
                                  widget=forms.Textarea(attrs={'rows': 20, 'cols': 70}))


class DeleteBookForm(forms.Form):

    author = forms.CharField(label='Автор', max_length=120, widget=forms.TextInput(attrs={'size': '68'}))
    book_name = forms.CharField(label='Название', max_length=120, widget=forms.TextInput(attrs={'size': '68'}))



