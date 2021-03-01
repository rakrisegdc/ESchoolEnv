from django.shortcuts import render
from .models import Subject, Standard, AcademicYear
from .forms import *
from django.views import generic
from django.http import HttpResponseRedirect
# Create your views here.

class SubjectListView(generic.ListView,generic.FormView):
    model = Subject
    template_name = 'academic_settings/subject.html'
    form_class = SubjectForm
    #paginate_by = 5  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('subjects')

# class SubjectAddForm(generic.FormView):
#     model = Subject
#     template_name = 'academic_settings/Add_Subject.html'
#     form_class = SubjectForm
#
#     def form_valid(self, form):
#         form.save()
#         return HttpResponseRedirect('subjects')

# class SubjectEditForm(generic.FormView):
#     module = Subject


class StandardListView(generic.ListView,generic.FormView):
    model = Standard
    template_name = 'academic_settings/standard.html'
    form_class = StandardForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('standards')



# class StandardAddForm(generic.FormView):
#     model = Standard
#     template_name = 'academic_settings/Add_Standard.html'
#     form_class = StandardForm
#
#     def form_valid(self, form):
#         form.save()
#         return HttpResponseRedirect('standards')

