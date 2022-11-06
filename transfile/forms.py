from django import forms
from .models import FileUpload

class TransFileForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sentence'].widget.attrs['class'] = 'mt-5'

    sentence = forms.CharField(label='翻訳(日本語)', widget=forms.Textarea(), required=True)
    
class UploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ('files',)