from django import forms
from .models import Entry

# New Page Form
class NewPageForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'content']    

# Edit Page Form
class EditPageForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'content']
