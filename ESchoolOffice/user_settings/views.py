from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Religion,Caste,State,Mothertongue,Relation

def usersettings(request):
    model_object = Religion.objects.all()
    model_object1 = Caste.objects.all()
    form = forms.ReligionForms()
    form1 = forms.CasteForms()
    form_context = {
        'form': form,
        'form1': form1,
    }
    data_context = {
        'data' : model_object ,
        'data1' : model_object1,
    }
    return render(request, 'user_settings/Religion.html', form_context, data_context)

def religion(request):
    model_object = Religion.objects.all()
    # model_object1 = Caste.objects.all()
    if request.method == 'POST':
        form = forms.ReligionForms(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('user_settings:ReligionForms')
    else:
        form = forms.ReligionForms()
        # form1 = forms.CasteForms()
    return render(request, 'user_settings/Religion.html', {'form': form, 'data': model_object})


def delete_religion(request,pk):
    post = get_object_or_404(Religion,pk= pk)
    post.delete()
    return redirect('user_settings:ReligionForms')

def edit_religion(request, pk):
    template = "user_settings/Religion.html"
    post = get_object_or_404(Religion, pk=pk)
    model_object = Religion.objects.all()
    if request.method == 'POST':
        form = forms.ReligionForms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('user_settings:ReligionForms')
    else:
        form = forms.ReligionForms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


def caste(request):
    model_object1 = Caste.objects.all()
    if request.method == 'POST':
        form1 = forms.CasteForms(request.POST, request.FILES)
        if form1.is_valid():
            instance = form1.save(commit=False)
            instance.save()
            return redirect('user_settings:CasteForms')
    else:
        form1 = forms.CasteForms()
    return render(request, 'user_settings/Religion.html', {'form1': form1, 'data1': model_object1})

def delete_caste(request,pk):
    post = get_object_or_404(Caste,pk= pk)
    post.delete()
    return redirect('user_settings:CasteForms')

def edit_caste(request, pk):
    template = "user_settings/Religion.html"
    post = get_object_or_404(Caste, pk=pk)
    model_object1 = Caste.objects.all()
    if request.method == 'POST':
        form1 = forms.CasteForms(request.POST, instance=post)
        if form1.is_valid():
            instance = form1.save(commit=False)
            instance.save()
            return redirect('user_settings:CasteForms')
    else:
        form1 = forms.CasteForms(instance=post)
        context = {
            'form1': form1,
            'post': post,
            'data1': model_object1,
        }
    return render(request, template, context)
