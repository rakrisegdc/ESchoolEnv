from django import forms
import models


class DesignationForm(forms.ModelForm):
    desig_name = forms.CharField(label="Designation", max_length=100, required=True)

    class Meta:
        model = models.Designation
        fields = ['desig_name']