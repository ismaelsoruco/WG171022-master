from django.conf.urls import url
from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name='calendar_by_user'),
    url(r'^all_events/', views.all_events, name='all_events'),
        # /apli/task
    url(r'^task/$', views.index_task, name='index_task'),
 
    # /task/13
    url(r'^task/(?P<pk>[0-9]+)/$', views.detail_task, name='detail_task'),

    # /proyecto/new/ TEST proyecto
    url(r'^task/new/$', views.new_task.as_view(), name='task_new'),

]