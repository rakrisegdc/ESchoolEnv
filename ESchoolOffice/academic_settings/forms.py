from django.forms import ModelForm, DateInput
from . models import Subject, AcademicYear, Standard, Division, Grade

class SubjectForm(ModelForm):
     class Meta:
         model = Subject
         fields = '__all__'


class AcademicYearForm(ModelForm):
    class Meta:
        model = AcademicYear
        fields = '__all__'
        widgets = {
            'acyear_startdate': DateInput(attrs={'type': 'date'}),
            'acyear_enddate': DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(AcademicYearForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

       # acyear_year
        # acyear_startdate
        # acyear_enddate

class StandardForm(ModelForm):
    class Meta:
        model = Standard
        fields = '__all__'


class DivisionForm(ModelForm):
    class Meta:
        model = Division
        fields = '__all__'


class GradeForm(ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'




