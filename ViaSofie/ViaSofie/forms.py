from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(label='Email address', max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'size': 150}))