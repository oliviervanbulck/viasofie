from django import forms
from nocaptcha_recaptcha.fields import NoReCaptchaField


class ContactForm(forms.Form):
    email = forms.EmailField(label='Email address', max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'size': 150}))
    attachment = forms.FileField(required=False, widget=forms.FileInput)
    captcha = NoReCaptchaField()




