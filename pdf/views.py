from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy #delete
from django.http import HttpResponse #pdf
from django.template.loader import get_template #pdf
from django.template import Context
from django.views.generic import View
from django.contrib.auth.decorators import login_required # requisito  login  def
from django.contrib.auth.mixins import LoginRequiredMixin # re quisito login  viw 
from django.db.models import Q # busqueda
from django.core.mail import send_mail # send email
from django.contrib import messages 
from django.conf import settings # mail
from django.http import HttpResponse

from .utils import render_to_pdf # PDF
from apli.models import Person, Project, Attachment, Assignment, Cost, Horaire
from django.http import HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from datetime import date
from django.core.files.base import ContentFile
from io import BytesIO
from xhtml2pdf import pisa



# Create your views here.
class GeneratePDF(View):
    def get(self, request, *args, **kwargs):

        project = get_object_or_404(Project, id=kwargs['pk'])
        if project.sort == "Angebot":
            template = get_template('menu/quotation/quotation.html')
            context = {"project": project, }
            html = template.render(context)
            pdf = render_to_pdf('menu/quotation/quotation.html', context)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "Invoice_%s.pdf" %("12341231")
                content = "inline; filename='%s'" %(filename)
                download = request.GET.get("download")
            if download:
                content = "attachment; filename='{Project.name} %s'" %(filename) #poner nombre de proyecto
                response['Content-Disposition'] = content

            return response
            return HttpResponse("Not found")
            
        if project.sort == "Auftrag":
            template = get_template('menu/sales_order/sales_order.html')
            context = {"project": project, }
            html = template.render(context)
            pdf = render_to_pdf('menu/sales_order/sales_order.html', context)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "Invoice_%s.pdf" %("12341231")
                content = "inline; filename='%s'" %(filename)
                download = request.GET.get("download")
            if download:
                content = "attachment; filename='{Project.name} %s'" %(filename) #poner nombre de proyecto
                response['Content-Disposition'] = content

            return response
            return HttpResponse("Not found")

        if project.sort == "Job":
            template = get_template('menu/sales_order/sales_order.html')
            context = {"project": project, }
            html = template.render(context)
            pdf = render_to_pdf('menu/sales_order/sales_order.html', context)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "Invoice_%s.pdf" %("12341231")
                content = "inline; filename='%s'" %(filename)
                download = request.GET.get("download")
            if download:
                content = "attachment; filename='{Project.name} %s'" %(filename) #poner nombre de proyecto
                response['Content-Disposition'] = content

            return response
            return HttpResponse("Not found")


class Rechnung(View):
    def get(self, request, *args, **kwargs):

        project = get_object_or_404(Project, id=kwargs['pk'])

        if project.sort == "Job":
            template = get_template('menu/rechnung_project/rechnung_project.html')
            context = {"project": project, }
            html = template.render(context)
            pdf = render_to_pdf('menu/rechnung_project/rechnung_project.html', context)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "Invoice_%s.pdf" %("12341231")
                content = "inline; filename='%s'" %(filename)
                download = request.GET.get("download")
            if download:
                content = "attachment; filename='{Project.name} %s'" %(filename) #poner nombre de proyecto
                response['Content-Disposition'] = content

            return response
            return HttpResponse("Not found")

