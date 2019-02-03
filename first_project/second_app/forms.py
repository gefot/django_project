from django import forms
from django.core import validators


def check_for_z(value):
    if value[0] != 'z':
        raise forms.ValidationError("NEEDS TO START WITH Z")


class FormName(forms.Form):
    mac_address = forms.CharField(max_length=15, validators=[validators.MaxLengthValidator(12)])
    description = forms.CharField(max_length=30)
    verify_description = forms.CharField(max_length=30, label="Enter description again")
    registration_status = forms.CharField(max_length=30)
    text = forms.CharField(widget=forms.Textarea)

    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    # name = forms.CharField(max_length=100)
    # email = forms.EmailField()
    # text = forms.CharField(widget=forms.Textarea)

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher
