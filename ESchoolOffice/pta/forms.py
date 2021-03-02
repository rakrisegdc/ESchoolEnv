from django.forms import ModelForm, SelectDateWidget, forms, DateInput
from .models import *


class PTADesignationForm(ModelForm):
    class Meta:
        model = PTADesignation
        fields = '__all__'


class CommitteeRegistrationForm(ModelForm):
    class Meta:
        model = CommitteeRegistration
        fields = '__all__'

        labels = {
            'academicyear': 'Academic Year',
            'ptadesignation': 'Designation (in PTA)',
            'parent': 'Parent',
            'comm_decision': 'Decisions Made',
        }

        def __init__(self, *args, **kwargs):
            super(CommitteeRegistrationForm, self).__init__(*args, **kwargs)
            self.fields['academicyear'].widget.attrs.update({'class': 'myfieldclass'})


class PTACommitteeForm(ModelForm):
    class Meta:
        model = PTACommittee
        fields = '__all__'

        labels = {
            'comm_date': 'Date',
            'committeeregistration': 'Members',
            'comm_agenda': 'Agenda',
            'comm_decision': 'Decisions Made',
        }

        widgets = {'comm_date': DateInput(attrs={'type': 'date'})}


class PTAAttendedMembersForm(ModelForm):
    class Meta:
        model = PTAAttendedMembers
        fields = '__all__'
