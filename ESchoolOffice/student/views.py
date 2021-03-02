from django.shortcuts import render, redirect, get_object_or_404
from .import forms
from .models import Student
from django.views import generic


class StudentList(generic.ListView):
    template_name = 'student/index.html'

    def get_queryset(self):
        return Student.objects.all()


class StudentView(generic.DetailView):
    model = Student
    template_name = 'student/StudentView.html'


# def index(request):
#     return render(request, 'student/index.html')


def studentregistration(request):
    model_object = Student.objects.all()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('student:StudentRegistration')
    else:
        form = forms.StudentForm()
    return render(request, 'student/Student.html', {'form': form, 'data': model_object})

