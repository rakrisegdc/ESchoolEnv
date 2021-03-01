from django import forms
from .import models


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = '__all__'
        widgets = {
            'stud_address': forms.Textarea(attrs={'cols': 40, 'rows': 4}),
            'stud_gender': forms.RadioSelect(choices=model.STUD_GENDER),
            'stud_bloodgroup' : forms.RadioSelect(choices=model.BLOOD_GROUP),
            'stud_dob': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'stud_regdate': forms.TextInput(attrs={'readonly':'readonly'})
        }



class StudentAcademicForm(forms.ModelForm):
    class Meta:
        model = models.StudentAcademic
        fields = '__all__'


class StudentMarksForm(forms.ModelForm):
    class Meta:
        model = models.StudentMarks
        fields = '__all__'
