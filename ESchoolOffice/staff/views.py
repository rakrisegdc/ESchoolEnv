from django.shortcuts import render
from django.http import HttpResponse


def designation(request):
    return HttpResponse('Designation')


def leavetype(request):
    return HttpResponse('Leave Type')


def staff(request):
    return HttpResponse("Staff details")


def staffleave(request):
    return HttpResponse("Staff Leave details")


def TeacherSubject(request):
    return HttpResponse('Teacher Sub')
