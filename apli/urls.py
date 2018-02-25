from django.conf.urls import url
from . import views



urlpatterns = [
    #ORDENAR ALFABETICAMENTE

   #ASSIGNMENT: index, detail, create, update, delete.
    url(r'^apli/leu/$', views.apli, name='apli'),

    url(r'^assignment/$', views.assignment_index, name='assignment_index'),

    url(r'^assignment/(?P<pk>[0-9]+)/$', views.assignment_detail, name='assignment_detail'),
    url(r'^assignment/new/$', views.AssignmentCreate.as_view(), name='assignment_new'),
    url(r'^assignment/(?P<pk>[0-9]+)/update/$', views.AssignmentUpdate.as_view(), name='assignment_update'),
    url(r'^assignment/(?P<pk>[0-9]+)/delete/$', views.AssignmentDelete.as_view(), name='assignment_delete'),
    url(r'^assignment/(?P<pk>[0-9]+)/send/$', views.assignment_timetable_send, name='assignment_timetable_send'),
	
    #BUSCAR 

    url(r'^busca/$', views.busca, name='busca'), 

    # COSTO
    url(r'^cost/(?P<pk>[0-9]+)/$', views.cost_detail, name='cost_detail'),
    url(r'^cost/$', views.cost_index, name='cost_index'),
    url(r'^cost/new/$', views.CostCreate.as_view(), name='cost_new'),
    url(r'^cost/(?P<pk>[0-9]+)/update/$', views.CostUpdate.as_view(), name='cost_update'),
    url(r'^cost/(?P<pk>[0-9]+)/delete/$', views.CostDelete.as_view(), name='cost_delete'),

	#DASHBOARD: index
	url(r'^dashboard/$', views.dashboard, name='dashboard'),

    # TIMETABLE HORAIRE
    url(r'^time/new/$', views.create_horaire_assignment.as_view(), name='create_horaire_assignment'),
    url(r'^time/(?P<pk>[0-9]+)/update/$', views.edit_horaire_assignment.as_view(), name='edit_horaire_assignment'),
    url(r'^time/(?P<pk>[0-9]+)/delete/$', views.delete_horaire_assignment.as_view(), name='delete_horaire_assignment'),

    # TIME work in generall 
    url(r'^timework/new/$', views.create_time_work.as_view(), name='create_time_work'),
    url(r'^timework/(?P<pk>[0-9]+)/update/$', views.edit_time_work.as_view(), name='edit_time_work'),
    url(r'^timework/(?P<pk>[0-9]+)/delete/$', views.delete_time_work.as_view(), name='delete_time_work'),



    #MAIL
    url(r'^project/(?P<pk>[0-9]+)/send/$', views.project_quotation_send, name='project_quotation_send'),
    #url(r'^mail_confirmation_work_to_model/$', views.mail_confirmation_work_to_model, name='mail_confirmation_work_to_model'),

	# PERSON: index, detail, create, update, delete.

	url(r'^person$', views.person_index, name='person_index'),
   # url(r'^person/(?P<slug>[\w-]+)/$', views.person_detail, name='person_detail'),
	url(r'^person/(?P<pk>[0-9]+)/$', views.person_detail, name='person_detail'),
    url(r'^person/new/$', views.PersonCreate.as_view(), name='person_new'),
    url(r'^person/(?P<pk>[0-9]+)/update/$', views.PersonUpdate.as_view(), name='person_update'),
    url(r'^person/(?P<pk>[0-9]+)/delete/$', views.PersonDelete.as_view(), name='person_delete'),

    # PROJECT: index, detail, create, update, delete.

    url(r'^project/$', views.project_index, name='project_index'),

    url(r'^project/(?P<pk>[0-9]+)/$', views.project_detail, name='project_detail'),
    url(r'^project/new/$', views.ProjectCreate.as_view(), name='project_new'),
    url(r'^project/(?P<pk>[0-9]+)/update/$', views.ProjectUpdate.as_view(), name='project_update'),
    url(r'^project/(?P<pk>[0-9]+)/delete/$', views.ProjectDelete.as_view(), name='project_delete'),

    url(r'^$', views.formset_view) 




]