from django.conf.urls import url
from .views import asset, edit_asset, delete_asset, merchant, index, edit_merchant, delete_merchant

app_name = 'asset'
urlpatterns = [
    url(r'^$', index, name='IndexForms'),
    url(r'/asset', asset, name='AssetForms'),
    url(r'edit_asset/(?P<pk>\d+)/$', edit_asset, name='edit_asset'),
    url(r'delete_asset/(?P<pk>\d+)/$', delete_asset, name='delete_asset'),
    url(r'merchant', merchant, name='MerchantForms'),
    url(r'edit_merchant/(?P<pk>\d+)/$', edit_merchant, name='edit_merchant'),
    url(r'delete_merchant/(?P<pk>\d+)/$', delete_merchant, name='delete_merchant'),
]
