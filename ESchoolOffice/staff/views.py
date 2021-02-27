from django.shortcuts import render
from django.http import HttpResponse
from . import form


def designation(request):
    forms = form.DesignationForm
    return render(request, 'staff/designation.html', {'form': forms})


def leavetype(request):
    forms = form.LeaveTypeForm
    return render(request, 'staff/leavetype.html', {'form': forms})


def staff(request):
    return HttpResponse("Staff details")


def staffleave(request):
    return HttpResponse("Staff Leave details")


def teachersubjects(request):
    return HttpResponse('Teacher Sub')
