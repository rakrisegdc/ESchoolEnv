from django.conf.urls import url
from .views import religion,edit_religion,delete_religion,caste,edit_caste,delete_caste,index,state,delete_state,edit_state,mothertongue,edit_mothertongue,delete_mothertongue,relation,edit_relation,delete_relation

app_name = 'user_settings'
urlpatterns = [
    url(r'^$', index, name='IndexForms'),
    url(r'/religion', religion, name='ReligionForms'),
    url(r'edit_religion/(?P<pk>\d+)/$', edit_religion, name='edit_religion'),
    url(r'delete_religion/(?P<pk>\d+)/$', delete_religion, name='delete_religion'),

    url(r'/caste', caste, name='CasteForms'),
    url(r'edit_caste/(?P<pk>\d+)/$', edit_caste, name='edit_caste'),
    url(r'delete_caste/(?P<pk>\d+)/$', delete_caste, name='delete_caste'),

    url(r'/state', state, name='StateForms'),
    url(r'edit_state/(?P<pk>\d+)/$', edit_state, name='edit_state'),
    url(r'delete_state/(?P<pk>\d+)/$', delete_state, name='delete_state'),

    url(r'/mothertongue', mothertongue, name='MothertongueForms'),
    url(r'edit_mothertongue/(?P<pk>\d+)/$', edit_mothertongue, name='edit_mothertongue'),
    url(r'delete_mothertongue/(?P<pk>\d+)/$', delete_mothertongue, name='delete_mothertongue'),

    url(r'/relation', relation, name='RelationForms'),
    url(r'edit_relation/(?P<pk>\d+)/$', edit_relation, name='edit_relation'),
    url(r'delete_relation/(?P<pk>\d+)/$', delete_relation, name='delete_relation'),
]