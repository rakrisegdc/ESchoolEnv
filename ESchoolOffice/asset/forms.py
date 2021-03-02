from django.forms import ModelForm
from django import forms
from .models import Stock, AssetManagementOut, AssetManagementDetails, AssetManagementIn, Asset, Merchant


class MerchantForms(ModelForm):
    class Meta:
        model = Merchant
        fields = '__all__'
        widgets = {
            'mer_address': forms.Textarea(attrs={'cols': 40, 'rows': 4})}


class AssetForms(ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'
        widgets = {
            'asset_description': forms.Textarea(attrs={'cols': 40, 'rows': 4})}


class AssetManagementInForms(ModelForm):
    class Meta:
        model = AssetManagementIn
        fields = '__all__'
        widgets = {'assetmgmtin_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'})}


class AssetManagementDetailsForms(ModelForm):
    class Meta:
        model = AssetManagementDetails
        fields = ['asset', 'assetdet_qty', 'assetdet_unitrate', 'assetdet_unit']


class AssetManagementOutForms(ModelForm):
    class Meta:
        model = AssetManagementOut
        fields = '__all__'


class StockForms(ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'
