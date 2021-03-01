from django.conf.urls import url
from .views import religion,edit_religion,delete_religion,caste,edit_caste,delete_caste,usersettings

app_name = 'user_settings'
urlpatterns = [
    url(r'^$', usersettings, name='UserSetingsForms'),
    # url(r'^$', religion, name='ReligionForms'),
    url(r'edit_religion/(?P<pk>\d+)/$', edit_religion, name='edit_religion'),
    url(r'delete_religion/(?P<pk>\d+)/$', delete_religion, name='delete_religion'),

    # url(r'^$', caste, name='CasteForms'),
    url(r'edit_caste/(?P<pk>\d+)/$', edit_caste, name='edit_caste'),
    url(r'delete_caste/(?P<pk>\d+)/$', delete_caste, name='delete_caste'),
]