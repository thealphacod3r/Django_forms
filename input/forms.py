from django import forms

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)
    
    #Added input files
