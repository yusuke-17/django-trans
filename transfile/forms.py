from django import forms
from .models import FileUpload

class TransFileForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ('uploadedFile',)