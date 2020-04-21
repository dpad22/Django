from django import forms
from .models import Book, Author

class BookForm(forms.Form):
    title = forms.CharField(label = 'newTitle', max_length=255)
    description = forms.CharField(label = 'newDescription', max_length=255)

