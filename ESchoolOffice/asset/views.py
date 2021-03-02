from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from . import forms
from .models import Asset, Merchant, AssetManagementIn, AssetManagementDetails, AssetManagementOut
from django.views.generic.edit import DeleteView


# index page

def index(request):
    return render(request, 'asset/index.html')


# asset create function


def asset(request):
    model_object = Asset.objects.all()
    if request.method == 'POST':
        form = forms.AssetForms(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect("asset:AssetForms")
    else:
        form = forms.AssetForms()
    return render(request, 'asset/asset.html', {'form': form, 'data': model_object})


# merchant create function


def merchant(request):
    model_object = Merchant.objects.all()
    if request.method == 'POST':
        form = forms.MerchantForms(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect("asset:MerchantForms")
    else:
        form = forms.MerchantForms()
    return render(request, 'asset/Merchant.html', {'form': form, 'data': model_object})

# asset inwards create function


# def asset_in(request):
#     model_object = AssetManagementIn.objects.all()
#
#     if request.method == 'POST':
#         form = forms.AssetManagementInForms(request.POST, request.FILES)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.save()
#             response = instance.id
#         return redirect("asset:AssetManagementDetailsForms", fk=response)
#     else:
#         form = forms.AssetManagementInForms()
#     return render(request, 'asset/AssetManagementIn.html', {'form': form, 'data': model_object})


# asset inwards details create function


def asset_in(request):
    model_objectassetin = AssetManagementIn.objects.all()
    model_objectdetails = AssetManagementDetails.objects.all()
    model_objectasset = Asset.objects.all()
    if request.method == "GET":
        # create the object - Actionform
        form = forms.AssetManagementInForms
        form2 = forms.AssetManagementDetailsForms
        # pass into it
        return render(request, 'asset/AssetManagementIn.html', {'form': form, 'form2': form2, 'data': model_objectassetin, 'data1': model_objectdetails, 'data2': model_objectasset})
    elif request.method == "POST":
        # take all of the user data entered to create a new action instance in the table
        form = forms.AssetManagementInForms(request.POST, request.FILES)
        form2 = forms.AssetManagementDetailsForms(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            instance = form.save(commit=False)
            instance1 = form2.save(commit=False)
            # set the action_id Foreignkey
            instance.id = instance1.action_id
            instance.save()
            instance1.save()
            return redirect("asset:AssetManagementDetailsForms")
        else:
            form = forms.AssetManagementInForms()
            form2 = forms.AssetManagementDetailsForms()
        return render(request, 'asset/AssetManagementIn.html', {'form': form, 'form2': form2})



# def asset_details(request):
#     model_object = AssetManagementDetails.objects.all()
#     model_objectasset = Asset.objects.all()
#     if request.method == 'POST':
#         form = forms.AssetManagementDetailsForms(request.POST, request.FILES)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.save()
#             # return redirect("asset/AssetDetails.html")
#             return render(request, 'asset:AssetManagementDetailsForms', {'form': form, 'data1': model_objectasset})
#     else:
#         form = forms.AssetManagementDetailsForms()
#     return render(request, 'asset/AssetDetails.html', {'form': form, 'data': model_object, 'data1': model_objectasset})


# asset delete function


def delete_asset(request, pk):
    post = get_object_or_404(Asset, pk=pk)
    post.delete()
    return redirect('asset:AssetForms')


# asset delete function


def edit_asset(request, pk):
    template = "asset/Asset.html"
    post = get_object_or_404(Asset, pk=pk)
    model_object = Asset.objects.all()
    if request.method == 'POST':
        form = forms.AssetForms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('asset:AssetForms')
    else:
        form = forms.AssetForms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


# merchant delete function


def merchant_delete(request, pk):
    post = get_object_or_404(Merchant, pk=pk)
    post.delete()
    return redirect('asset:MerchantForms')


# merchant edit function


def merchant_edit(request, pk):
    template = "asset/Merchant.html"
    post = get_object_or_404(Merchant, pk=pk)
    model_object = Merchant.objects.all()
    if request.method == 'POST':
        form = forms.MerchantForms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('asset:MerchantForms')
    else:
        form = forms.MerchantForms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


# Asset edit function


class AssetView(generic.DetailView):
    model = Asset
    template_name = 'asset/AssetView.html'


# Merchant edit function

class MerchantView(generic.DetailView):
    model = Merchant
    template_name = 'asset/MerchantView.html'





