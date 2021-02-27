from django.conf.urls import url
from .views import asset

app_name = 'asset'
urlpatterns = [
    url(r'^$', asset, name='AssetForms'),
]
