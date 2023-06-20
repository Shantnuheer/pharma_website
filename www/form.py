from django import forms
from .models import fromula,contact,cart


class formulaform(forms.ModelForm):
    class Meta:
        model = fromula
        fields = '__all__'

class contactform(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'

class cartform(forms.ModelForm):
    class Meta:
        model = cart
        fields = '__all__'