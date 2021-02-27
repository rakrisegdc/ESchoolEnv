from django.shortcuts import render
from .models import Subject
from .import forms

# Create your views here.


def addsubject(request):
    form = forms.SubjectForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}
    return render(request, 'academic_settings/Add_Subject.html', context)

def indexsubjects(request):
    subjects = Subject.objects.all()
    return render(request, 'academic_settings/Index_Subject.html',)
