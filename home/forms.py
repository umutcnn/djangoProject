from django import forms

class searchs(forms.Form):
    query=forms.CharField(label='Search',max_length=100)