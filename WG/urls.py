from django.conf.urls import url, include   
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^apli/', include('apli.urls')),
    url(r'^calendar/', include('fullcalendar.urls')),
    url(r'^register/', include('register.urls')),
    url(r'^pdf/', include('pdf.urls')),
]
