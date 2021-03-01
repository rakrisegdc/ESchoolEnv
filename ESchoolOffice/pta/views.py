from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import generic

from .forms import *


class PTADesignationForm(generic.FormView):
    model = PTADesignation
    template_name = 'pta\PTADesignation.html'
    form_class = PTADesignationForm

    def form_valid(self, form):
        form.save()
        return HttpResponse("Saved")


class PTADesignationIndexView(generic.ListView):
    template_name = 'pta\PTADesignationIndex.html'
    context_object_name = 'pta_designation_list'

    def get_queryset(self):
        return PTADesignation.objects.all()


class PTADesignationDetailView(generic.DetailView):
    model = PTADesignation
    template_name = 'pta/PTADesignationView.html'


class CommiteeRegistration(generic.ListView):
    template_name = 'pta\PTACommiteeRegisration.html'
    context_object_name = 'commitee_registration_list'

    def get_queryset(self):
        return CommiteeRegistration.objects.all()


class CommiteeRegistrationDetail(generic.DetailView):
    model = CommiteeRegistration
    template_name = 'pta/PTACommiteeRegistrationDetail.html'


class CommiteeRegistrationForm(generic.FormView):
    model = CommitteeRegistration
    template_name = 'pta/PTACommiteeRegistrationForm.html'
    form_class = CommitteeRegistrationForm

    def form_valid(self, form):
        form.save()
        return HttpResponse("Saved")
