from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Asset


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
    return render(request, 'asset/Asset.html', {'form': form, 'data': model_object})


