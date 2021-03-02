from django import forms
from .import models

# class UserSettingsForms(form.ModelForm):
#     class Meta:
#         model = models.Religion


class ReligionForms(forms.ModelForm):
    class Meta:
        model = models.Religion
        fields = '__all__'

class CasteForms(forms.ModelForm):
    class Meta:
        model = models.Caste
        fields = '__all__'

class StateForms(forms.ModelForm):
    class Meta:
        model = models.State
        fields = '__all__'

class MothertongueForms(forms.ModelForm):
    class Meta:
        model = models.Mothertongue
        fields = '__all__'

class RelationForms(forms.ModelForm):
    class Meta:
        model = models.Religion
        fields = '__all__'
