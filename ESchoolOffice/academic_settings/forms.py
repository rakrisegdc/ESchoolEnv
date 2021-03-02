from django.forms import ModelForm
from . models import Subject, AcademicYear, Standard, Division, Grade

class SubjectForm(ModelForm):
     class Meta:
         model = Subject
         fields = '__all__'

class AcademicYearForm(ModelForm):
    class Meta:
        model = AcademicYear
        fields = '__all__'

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




