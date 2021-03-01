from django.shortcuts import render, redirect, get_object_or_404
from .import forms
from .models import Student


def index(request):
    return render(request, 'student/index.html')


def studentregistration(request):
    model_object = Student.objects.all()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('student:StudentForm')
    else:
        form = forms.StudentForm()
    return render(request, 'student/Student.html', {'form': form, 'data': model_object})

