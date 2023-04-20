from django import forms
class TopicForms(forms.Form):
    tname=forms.CharField(max_length=100)

class WebpageForms(forms.Form):
    tname=forms.CharField(max_length=100)
    name=forms.CharField(max_length=100)
    url=forms.URLField()
    
class AccessRecordForms(forms.Form):
    name=forms.CharField(max_length=100)
    author=forms.CharField(max_length=100)
    date=forms.DateField()
    