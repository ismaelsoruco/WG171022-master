from django.contrib import admin
from .models import  Project, Attachment, Person, Assignment, Horaire, Cost, Time


admin.site.register(Project)
admin.site.register(Attachment)
admin.site.register(Person)
admin.site.register(Assignment)
admin.site.register(Horaire)
admin.site.register(Cost)
admin.site.register(Time)