from django.forms import ModelForm
from .models import Pettycash, Pettycashapproval


class PettycashForm(ModelForm):
    class Meta:
        model = Pettycash
        fields = '__all__'


class PettycashapprovalForm(ModelForm):
    class Meta:
        model = Pettycashapproval
        fields = '__all__'
