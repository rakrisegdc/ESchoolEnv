from django.shortcuts import render
from .models import Subject, Standard, AcademicYear
from .import forms
from django.views import generic
from django.http import HttpResponseRedirect

# Create your views here.

# Create your views here.
class IndexView(generic.ListView):
    model = Subject
    context_object_name = 'subject_list'
    template_name = 'academic_settings/Index_Subject.html'

    def get_queryset(self):
        return Subject.objects.all()


def addsubject(request):
    form = forms.SubjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'academic_settings/Index_Subject.html')
    context = {'form': form}
    return render(request, 'academic_settings/Add_Subject.html', context)

def indexsubjects(request):
    subjects = Subject.objects.all()
    return render(request, 'academic_settings/Index_Subject.html')



def addacyear(request):
    form = forms.AcademicYearForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'academic_settings/Index_AcademicYear.html')
    context = {'form': form}
    return render(request, 'academic_settings/Add_AcademicYear.html', context)

def indexacyear(request):
    addacyear = AcademicYear.objects.all()
    return render(request, 'academic_settings/Index_Subject.html')


def addstandard(request):
    form = forms.StandardForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'academic_settings/Index_Subject.html')
    context = {'form': form}
    return render(request, 'academic_settings/Add_Standard.html', context)

def indexstandard(request):
    standard = Standard.objects.all()
    return render(request, 'academic_settings/Index_Standard.html')
