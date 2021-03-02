from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Religion,Caste,State,Mothertongue,Relation

# def usersettings(request):
#     model_object = Religion.objects.all()
#     model_object1 = Caste.objects.all()
#     form = forms.ReligionForms()
#     form1 = forms.CasteForms()
#     form_context = {
#         'form': form,
#         'form1': form1,
#     }
#     data_context = {
#         'data' : model_object ,
#         'data1' : model_object1,
#     }
#     return render(request, 'user_settings/Religion.html', form_context, data_context)

def index(request):
    return render(request, 'user_settings/index.html')


def religion(request):
    model_object = Religion.objects.all()
    if request.method == 'POST':
        form = forms.ReligionForms(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('user_settings:ReligionForms')
    else:
        form = forms.ReligionForms()
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
    model_object = Caste.objects.all()
    if request.method == 'POST':
        form = forms.CasteForms(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('user_settings:CasteForms')
    else:
        form = forms.CasteForms()
    return render(request, 'user_settings/Caste.html', {'form': form, 'data': model_object})

def delete_caste(request,pk):
    post = get_object_or_404(Caste,pk= pk)
    post.delete()
    return redirect('user_settings:CasteForms')

def edit_caste(request, pk):
    template = "user_settings/Caste.html"
    post = get_object_or_404(Caste, pk=pk)
    model_object = Caste.objects.all()
    if request.method == 'POST':
        form = forms.CasteForms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('user_settings:CasteForms')
    else:
        form = forms.CasteForms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data1': model_object,
        }
    return render(request, template, context)


def state(request):
    model_object = State.objects.all()
    if request.method == 'POST':
        form = forms.StateForms(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('user_settings:StateForms')
    else:
        form = forms.StateForms()
    return render(request, 'user_settings/State.html', {'form': form, 'data': model_object})

def delete_state(request,pk):
    post = get_object_or_404(State,pk= pk)
    post.delete()
    return redirect('user_settings:StateForms')

def edit_state(request, pk):
    template = "user_settings/State.html"
    post = get_object_or_404(State, pk=pk)
    model_object = State.objects.all()
    if request.method == 'POST':
        form = forms.StateForms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('user_settings:StateForms')
    else:
        form = forms.StateForms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data1': model_object,
        }
    return render(request, template, context)


def mothertongue(request):
    model_object = Mothertongue.objects.all()
    if request.method == 'POST':
        form = forms.MothertongueForms(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('user_settings:MothertongueForms')
    else:
        form = forms.MothertongueForms()
    return render(request, 'user_settings/MotherTongue.html', {'form': form, 'data': model_object})

def delete_mothertongue(request,pk):
    post = get_object_or_404(Mothertongue,pk= pk)
    post.delete()
    return redirect('user_settings:MothertongueForms')

def edit_mothertongue(request, pk):
    template = "user_settings/MotherTongue.html"
    post = get_object_or_404(Mothertongue, pk=pk)
    model_object = Mothertongue.objects.all()
    if request.method == 'POST':
        form = forms.MothertongueForms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('user_settings:MothertongueForms')
    else:
        form = forms.MothertongueForms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data1': model_object,
        }
    return render(request, template, context)



def relation(request):
    model_object = Relation.objects.all()
    if request.method == 'POST':
        form = forms.RelationForms(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('user_settings:RelationForms')
    else:
        form = forms.RelationForms()
    return render(request, 'user_settings/Relation.html', {'form': form, 'data': model_object})

def delete_relation(request,pk):
    post = get_object_or_404(Relation,pk= pk)
    post.delete()
    return redirect('user_settings:RelationForms')

def edit_relation(request, pk):
    template = "user_settings/Relation.html"
    post = get_object_or_404(Relation, pk=pk)
    model_object = Relation.objects.all()
    if request.method == 'POST':
        form = forms.RelationForms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('user_settings:RelationForms')
    else:
        form = forms.RelationForms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data1': model_object,
        }
    return render(request, template, context)