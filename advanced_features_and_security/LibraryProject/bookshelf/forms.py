from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Email Address')
    message = forms.CharField(widget=forms.Textarea, label='Message')