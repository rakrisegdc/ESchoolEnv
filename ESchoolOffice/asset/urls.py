from django.conf.urls import url
from django.urls import path

from .views import asset, edit_asset, delete_asset, merchant, index, merchant_edit, merchant_delete
from . import views

app_name = 'asset'
urlpatterns = [
    url(r'^$', index, name='IndexForms'),
    url(r'/asset', asset, name='AssetForms'),
    url(r'edit_asset/(?P<pk>\d+)/$', edit_asset, name='edit_asset'),
    url(r'delete_asset/(?P<pk>\d+)/$', delete_asset, name='delete_asset'),
    url(r'/merchant', merchant, name='MerchantForms'),
    url(r'merchant_edit/(?P<pk>\d+)/$', merchant_edit, name='merchant_edit'),
    url(r'merchant_delete/(?P<pk>\d+)/$', merchant_delete, name='merchant_delete'),
    path('asset_detail/<int:pk>/', views.AssetView.as_view(), name='asset_detail'),
    path('merchant_detail/<int:pk>/', views.MerchantView.as_view(), name='merchant_detail'),
]
