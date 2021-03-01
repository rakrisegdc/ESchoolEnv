from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import *

# PTADesignation


class PTADesignationList(generic.ListView):
    template_name = 'pta\PTADesignationIndex.html'
    # context_object_name = 'pta_designation_list'

    def get_queryset(self):
        return PTADesignation.objects.all()


class PTADesignationForm(generic.FormView):
    model = PTADesignation
    template_name = 'pta\PTADesignation.html'
    form_class = PTADesignationForm

    def form_valid(self, form):
        form.save()
        return HttpResponse("Saved")


class PTADesignationView(generic.DetailView):
    model = PTADesignation
    template_name = 'pta/PTADesignationView.html'


class PTADesignationDelete(generic.DeleteView):
    model = PTADesignation
    template_name = 'pta/PTDesignationDelete.html'
    success_url = reverse_lazy('pta:des_index')


class PTADesignationUpdate(generic.UpdateView):
    model = PTADesignation
    fields = ['pta_designation_name']
    template_name = 'pta/PTADesignationUpdate.html'

# Commitee Registration


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
