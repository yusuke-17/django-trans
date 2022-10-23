from django import forms

class TransFileForm(forms.Form):
    sentence = forms.CharField(label='翻訳(日本語)', widget=forms.Textarea(), required=True)