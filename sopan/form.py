from django import forms

from sopan.models import Save


class wiproForm(forms.ModelForm):
    class Meta:
        model=Save
        fields='__all__'