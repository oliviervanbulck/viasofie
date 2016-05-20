from django import forms
from nocaptcha_recaptcha.fields import NoReCaptchaField


class ContactFormDossier(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'size': 150}))
    captcha = NoReCaptchaField()
