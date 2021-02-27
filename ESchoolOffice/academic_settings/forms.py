from django.forms import ModelForm
from . models import Subject,AcademicYear,Standard

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



