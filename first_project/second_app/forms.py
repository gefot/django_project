from django import forms
from django.core import validators
from second_app.models import User


class DeviceForm(forms.Form):
    mac_address = forms.CharField(max_length=15, validators=[validators.MaxLengthValidator(12)])
    description = forms.CharField(max_length=30)
    verify_description = forms.CharField(max_length=30, label="Enter description again")
    registration_status = forms.CharField(max_length=30)
    text = forms.CharField(widget=forms.Textarea)

    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])


class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
