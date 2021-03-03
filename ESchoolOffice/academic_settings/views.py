from django.shortcuts import  get_object_or_404, redirect
from .forms import *
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

class SubjectListView(generic.ListView):
    model = Subject
    template_name = 'academic_settings/subjects_list.html'
    #paginate_by = 5  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SubjectAddForm(generic.FormView):
    model = Subject
    template_name = 'academic_settings/subject_add.html'
    form_class = SubjectForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request,'successfully inserted')
        return HttpResponseRedirect('subjects')

# def subject_edit(request, id):
#     template = "academic_settings/subject_edit.html"
#     object = get_object_or_404(Subject, pk=id)
#     model_object = Subject.objects.all()
#     if request.method == 'POST':
#         form = SubjectForm(request.POST, instance=object)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.save()
#             return redirect('user_settings:StateForms')
#     else:
#         form = SubjectForm(instance=post)
#         context = {
#             'form': form,
#             'post': object,
#             'data1': model_object,
#         }
#     return render(request, template, context)

def delete_subject(request, id):
    obj = get_object_or_404(Subject, pk=id)
    obj.delete()
    return HttpResponseRedirect('/academics/subjects')

class StandardListView(generic.ListView):
    model = Standard
    template_name = 'academic_settings/standard_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class StandardAddForm(generic.FormView):
    model = Standard
    template_name = 'academic_settings/standard_add.html'
    form_class = StandardForm

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('standards')

def delete_standard(request, id):
    obj = get_object_or_404(Standard, pk=id)
    obj.delete()
    return HttpResponseRedirect('/academics/standards')

class DivisionListView(generic.ListView):
    model = Division
    template_name = 'academic_settings/division_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DivisionAddForm(generic.FormView):
    model = Division
    template_name = 'academic_settings/division_add.html'
    form_class = DivisionForm

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('divisions')

def delete_division(request, id):
    obj = get_object_or_404(Division, pk=id)
    obj.delete()
    return HttpResponseRedirect('/academics/divisions')

class GradeListView(generic.ListView):
    model = Grade
    template_name = 'academic_settings/grade_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GradeAddForm(generic.FormView):
    model = Grade
    template_name = 'academic_settings/grade_add.html'
    form_class = GradeForm

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('grades')

def delete_grade(request, id):
    obj = get_object_or_404(Grade, pk=id)
    obj.delete()
    return HttpResponseRedirect('/academics/grades')

class AcademicYearListView(generic.ListView):
    model = AcademicYear
    template_name = 'academic_settings/academicyear_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return  context

class AcademicYearAddForm(generic.FormView):
    model = AcademicYear
    template_name = 'academic_settings/academicyear_add.html'
    form_class = AcademicYearForm

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('acyear')

def delete_acyear(request, id):
    obj = get_object_or_404(AcademicYear, pk=id)
    obj.delete()
    return HttpResponseRedirect('/academics/acyear')

