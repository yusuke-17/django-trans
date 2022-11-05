from django import forms

class TransFileForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sentence'].widget.attrs['class'] = 'mt-5'

    sentence = forms.CharField(label='翻訳(日本語)', widget=forms.Textarea(), required=True)