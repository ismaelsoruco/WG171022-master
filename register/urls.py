from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views



urlpatterns = [


	# LOGIN / OUT 
	url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
	url(r'^logout/$', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),

	# REGISTER
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
	url(r'^account_activation_complete/$', views.account_activation_complete, name='account_activation_complete'),
	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),


	# RESET PASSWORD
	url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
	#url('^', include('django.contrib.auth.urls')), #este url, incluye todo lo anteriormente expuesto. 
	# no logro hacer que se vean las vistas que yo quiero hacer


		
	]
