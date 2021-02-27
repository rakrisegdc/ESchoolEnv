from django import forms
from .import models


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = '__all__'
        widgets = {
            'stud_address': forms.Textarea(attrs={'cols': 40, 'rows': 4}),
            'stud_gender': forms.RadioSelect(choices=model.STUD_GENDER),

        }


class StudentAcademicForm(forms.ModelForm):
    class Meta:
        model = models.StudentAcademic
        fields = '__all__'


class StudentMarksForm(forms.ModelForm):
    class Meta:
        model = models.StudentMarks
        fields = '__all__'
