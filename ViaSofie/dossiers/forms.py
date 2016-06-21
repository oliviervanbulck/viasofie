from django import forms
from nocaptcha_recaptcha.fields import NoReCaptchaField


# Formulier voor contact via dossier
class ContactFormDossier(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'size': 150}))
    attachment = forms.FileField(required=False, widget=forms.FileInput)
    captcha = NoReCaptchaField()
