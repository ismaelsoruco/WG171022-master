# -*- coding: utf-8 -*-
from django.db import models
from apli.models import Project
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# import datetime


class CalendarEvent(models.Model):
    title = models.CharField(_('Title'), blank=True, max_length=200)
    start = models.DateTimeField(_('Start'))
    end = models.DateTimeField(_('End'))
    all_day = models.BooleanField(_('All day'), default=False)
    url = models.CharField(_('Url'), blank=True, max_length=200)
    color = models.CharField(_('Color'), blank=True, max_length=200)
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    comment = models.CharField(blank=True, max_length=500)
    STATUS_CHOICES = (
        ('Not Started', 'Not Started'),
        ('Started', 'Started'),
        ('Finished', 'Finished'),
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Not Started')

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    def __unicode__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('detail_task', kwargs={'pk': self.pk})

    def __str__(self):
        # datita = datetime.datetime.strptime(self.start.string, "%Y-%m-%d").date()
        return self.title
