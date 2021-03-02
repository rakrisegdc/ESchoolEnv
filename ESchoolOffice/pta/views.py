from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import *


# region PTADesignation
class PTADesignationList(generic.ListView):
    template_name = 'pta\PTADesignationIndex.html'

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
# endregion


# region Committee Registration
class CommitteeRegistrationList(generic.ListView):
    template_name = 'pta\PTACommiteeRegisration.html'
    context_object_name = 'committee_registration_list'

    def get_queryset(self):
        return CommitteeRegistration.objects.all()


class CommitteeRegistrationView(generic.DetailView):
    model = CommitteeRegistration
    template_name = 'pta/PTACommiteeRegistrationDetail.html'


class CommitteeRegistrationForm(generic.FormView):
    model = CommitteeRegistration
    template_name = 'pta/PTACommiteeRegistrationForm.html'
    form_class = CommitteeRegistrationForm

    def form_valid(self, form):
        form.save()
        return HttpResponse("Saved")


class CommitteeRegistrationDelete(generic.DeleteView):
    model = CommitteeRegistration
    template_name = 'pta/PTACommiteeRegDelete.html'
    success_url = reverse_lazy('pta:reg_index')


class CommitteeRegistrationUpdate(generic.UpdateView):
    model = PTADesignation
    fields = ['academicyear', 'ptadesignation', 'parent']
    template_name = 'pta/PTACommitteeRegUpdate.html'
# endregion


# region PTACommittee
class PTACommitteeList(generic.ListView):
    template_name = 'pta\PTACommiteeIndex.html'

    def get_queryset(self):
        return PTACommittee.objects.all()


class PTACommitteeForm(generic.FormView):
    model = PTACommittee
    template_name = 'pta\PTACommitteeForm.html'
    form_class = PTACommitteeForm

    def form_valid(self, form):
        form.save()
        return HttpResponse("Saved")


class PTACommitteeView(generic.DetailView):
    model = PTACommittee
    template_name = 'pta/PTACommitteeView.html'


class PTACommitteeDelete(generic.DeleteView):
    model = PTACommittee
    template_name = 'pta/PTACommitteeDelete.html'
    success_url = reverse_lazy('pta:des_index')


class PTACommitteeUpdate(generic.UpdateView):
    model = PTACommittee
    fields = ['comm_date', 'committeeregistration', 'comm_agenda', 'comm_decision']
    template_name = 'pta/PTACommitteeUpdate.html'
# endregion

