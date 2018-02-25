# Python first
# django second
# your apps
# local directory 


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required # requisito login  def
from django.contrib.auth.mixins import LoginRequiredMixin # requisito login  viw 
from django.db.models import Q # busqueda
from django.views.generic import View
from .models import Person, Project, Attachment, Assignment, Horaire, Cost, Time
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect


# para las tablas + render tbn (za esta)
from django_tables2 import RequestConfig #TABLA
from .tables import PersonTable #TaBLA 

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# para mandar email
from django.core.mail import send_mail # send email
from django.contrib import messages 
from django.conf import settings # mail
from django.core.mail import EmailMultiAlternatives # mail
from django.template.loader import get_template #PDF
from io import BytesIO #pdf
from xhtml2pdf import pisa # pdf
from datetime import date #pdf ocupa date
from django.core.files.base import ContentFile #Adjuntar pdf email algo asi


#froms

from apli.forms import PersonForm, ProjectForm, CostForm, AttachmentForm, HoraireForm, AssignmentForm, TimeForm

#--------------------------
# INDICE (ordenar alfabéticamente)
# 1-assignment 
# 2- Buscar    ...linea
# 3- COSTO
# 4- dashboard ...linea 
# 5- MAIL
# 6- PERSON    ...linea 
# 7- Project   ...linea 
# -------------------------



def formset_view(request):

    return render(request, "formset_view.html",{})

def apli(request):

    return render(request, "menu/apli.html")





 ############################################################
#ASSIGNMENT

@login_required(login_url='/register/login/')
def assignment_index(request):
    all_assignments = Assignment.objects.all().filter(sort='')
    return render(request, 'apli/menu/assignment/assignments_index.html', {'all_assignments': all_assignments})

@login_required(login_url='/register/login/')
def assignment_detail(request, pk):
    assignment = get_object_or_404(Assignment, id=pk)
    all_horaire = assignment.horaire_set.all()
    return render(request, 'apli/menu/assignment/assignment_detail.html', {'assignment': assignment, 'all_horaire': all_horaire})

class AssignmentCreate(LoginRequiredMixin, CreateView):

    template_name = "apli/assignment_form.html"
    form_class = AssignmentForm
    

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return  super(AssignmentCreate, self).form_valid(form)
    
        # labels = {
        #         'comment_WG': "this is the model"
        # }
        # help_text = {
        #         'comment_WG': "this is the model"
        # }
        # error_messages = {
        #         'comment_WG': {
        #         #"required": "is required"
        #         }
        # }

class AssignmentUpdate(LoginRequiredMixin, UpdateView):
    model = Assignment
    template_name = "apli/assignment_form.html"
    form_class = AssignmentForm

    def form_valid(self, form):
        form.instance.last_edited_by = self.request.user

        return  super(AssignmentUpdate, self).form_valid(form)

    


class AssignmentDelete(LoginRequiredMixin, DeleteView):
    model = Assignment
    success_url = reverse_lazy('assignment_index')



def assignment_timetable_send(request, pk):
    assignment = get_object_or_404(Assignment, id=pk)

    all_persons = project.assignment_set.all()
    all_attachments = project.attachment_set.all()
    all_costs = project.cost_set.all()

    # debo crear el attachment
    template = get_template('menu/timetable_model/timetable_model.html')
    context = {"project": project, }
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)

    at = Attachment(project=project, sort=project.sort, send_date = date.today())

    at.file.save('nombre.pdf', ContentFile(result.getvalue()))
    at.save()

    context2 = {"project": project, }
    subject, from_email, to = 'ANGEBOT', 'base.EMAIL_HOST_USER', project.client.email
    text_content = 'This is an important message.'
    htmly = get_template('apli/menu/mail/mail_cotization.html')
    html_content = htmly.render(context2)
    msg = EmailMultiAlternatives(subject, html_content, from_email, [to])   
    reply_to=["ismaelsorucoi@gmail.com"] 
    msg.attach_alternative(html_content, "text/html")
    msg.attach(at.file.name, result.getvalue(), )
    msg.send()
    return render(request, 'apli/menu/project/project_detail.html', {'project': project, 'all_persons': all_persons, 'all_attachments': all_attachments, 'all_costs': all_costs})
   
    




 ############################################################
#  BUSCAR

@login_required(login_url='/register/login/')
def busca(request):
    query = request.GET.get("q")
    querysetAssignments = Assignment.objects.all()
    if query:
        querysetAssignments = querysetAssignments.filter(
            Q(id__icontains=query)
        ).distinct()

    querysetPersons = Person.objects.all()
    if query:
        querysetPersons = querysetPersons.filter(
            Q(name__icontains=query)|
            Q(email__icontains=query)
        ).distinct()

    querysetProjects = Project.objects.all()
    if query:
        querysetProjects = querysetProjects.filter(
            Q(name__icontains=query)
        ).distinct()

    return render(request, 'apli/menu/busca/busca.html', {"busca_assignment": querysetAssignments, "busca_persons": querysetPersons, "busca_projects": querysetProjects})
 

 ############################################################

 #COSTO: index, detail, create, update, delete.       
@login_required(login_url='/register/login/')
def cost_index(request):
    all_costs = Cost.objects.all().filter(sort='')
    return render(request, 'apli/cost/cost_index.html', {'all_costs': all_costs})

@login_required(login_url='/register/login/')
def cost_detail(request, pk):
    cost = get_object_or_404(Cost, id=pk)
    return render(request, 'apli/menu/cost/cost_detail.html', {'cost': cost})

class CostCreate(LoginRequiredMixin, CreateView):
    template_name = "apli/cost_form.html"
    form_class = CostForm

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return  super(CostCreate, self).form_valid(form)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
 

class CostUpdate(LoginRequiredMixin, UpdateView):
    model = Cost
    template_name = "apli/cost_form.html"
    form_class = CostForm

    def form_valid(self, form):
        form.instance.last_edited_by = self.request.user
        return  super(CostUpdate, self).form_valid(form)



class CostDelete(LoginRequiredMixin, DeleteView):
    model = Cost
    success_url = reverse_lazy('cost_index')

##############################################################

#  DASHBOARD 

@login_required(login_url='/register/login/')
def dashboard(request):
    all_projects    = Project.objects.all()
    all_persons     = Person.objects.all()
    
    
    return render(request, 'apli/menu/dashboard/dashboard.html', {'all_projects': all_projects, 'all_persons': all_persons})
#################################################################




#HORAIRE assignment

class create_horaire_assignment(LoginRequiredMixin, CreateView):

    template_name = "apli/horaire_form.html"
    form_class = HoraireForm

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return  super(create_horaire_assignment, self).form_valid(form)
       


class edit_horaire_assignment(LoginRequiredMixin, UpdateView):

    model = Horaire
    template_name = "apli/horaire_form.html"
    form_class = HoraireForm

    def form_valid(self, form):
        form.instance.last_edited_by = self.request.user
        return  super(edit_horaire_assignment, self).form_valid(form)




class delete_horaire_assignment(LoginRequiredMixin, DeleteView):
    model = Horaire
    success_url = reverse_lazy('index_project')
###################################################################

#TIME WORK 

class create_time_work(LoginRequiredMixin, CreateView):

    template_name = "apli/time_form.html"
    form_class = TimeForm

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return  super(create_time_work, self).form_valid(form)
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
 
class edit_time_work(LoginRequiredMixin, UpdateView):

    model = Time
    template_name = "apli/time_form.html"
    form_class = TimeForm

    def form_valid(self, form):
        form.instance.last_edited_by = self.request.user
        return  super(edit_time_work, self).form_valid(form)

class delete_time_work(LoginRequiredMixin, DeleteView):
    model = Time
    success_url = reverse_lazy('index_project')



###############################################################

# MAIL MAIL MAIL 

def mail_confirmation_work_to_model(request):
    return render(request, 'apli/menu/mail/mail_confirmation_work_to_model.html')

def project_quotation_send(request, pk):
    project = get_object_or_404(Project, id=pk)
    

    if project.sort == "Angebot":
        all_persons = project.assignment_set.all()
        all_attachments = project.attachment_set.all()
        all_costs = project.cost_set.all()

        # debo crear el attachment
        template = get_template('menu/quotation/quotation.html')
        context = {"project": project, }
        html = template.render(context)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)

        at = Attachment(project=project, sort=project.sort, send_date = date.today())

        at.file.save('nombre.pdf', ContentFile(result.getvalue()))
        at.save()

        context2 = {"project": project, }
        subject, from_email, to = 'ANGEBOT', 'base.EMAIL_HOST_USER', project.client.email
        text_content = 'This is an important message.'
        htmly = get_template('apli/menu/mail/mail_cotization.html')
        html_content = htmly.render(context2)
        msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
        reply_to=["ismaelsorucoi@gmail.com"] 
        msg.attach_alternative(html_content, "text/html")
        msg.attach(at.file.name, result.getvalue(), )
        msg.send()
        return render(request, 'apli/menu/project/project_detail.html', {'project': project, 'all_persons': all_persons, 'all_attachments': all_attachments, 'all_costs': all_costs})
    

    if project.sort == "Auftrag":
        all_persons = project.assignment_set.all()
        all_attachments = project.attachment_set.all()
        all_costs = project.cost_set.all()

        # debo crear el attachment
        template = get_template('menu/sales_order/sales_order.html')
        context = {"project": project, }
        html = template.render(context)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)

        at = Attachment(project=project, sort=project.sort, send_date = date.today())

        at.file.save('nombre.pdf', ContentFile(result.getvalue()))
        at.save()

        context2 = {"project": project, }
        subject, from_email, to = 'new angebot', 'base.EMAIL_HOST_USER', project.client.email
        text_content = 'This is an important message.'
        htmly = get_template('apli/menu/mail/mail_sales_order.html')
        html_content = htmly.render(context2)
        msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
        reply_to=["ismaelsorucoi@gmail.com"] 
        msg.attach_alternative(html_content, "text/html")
        msg.attach(at.file.name, result.getvalue(), )
        msg.send()
        return render(request, 'apli/menu/project/project_detail.html', {'project': project, 'all_persons': all_persons, 'all_attachments': all_attachments, 'all_costs': all_costs})



#####################################################################
#  PERSON: index, detail, create, update, delete.

@login_required(login_url='/register/login/')
def person_index(request):
     all_persons = Person.objects.all()
     return render(request, 'apli/menu/person/person_index.html', {'all_persons': all_persons})


    # table = PersonTable(Person.objects.all())
    # RequestConfig(request).configure(table)
    #return render(request, 'apli/menu/person/person_index.html', {'table': table})
    

@login_required(login_url='/register/login/')
def person_detail(request, pk):
    person = get_object_or_404(Person, id=pk)
    all_projects = person.project_set.all()
    return render(request, 'apli/menu/person/person_detail.html', {'person': person, 'all_projects': all_projects})


class PersonCreate(LoginRequiredMixin, CreateView):

    template_name = "apli/person_form.html"
    form_class = PersonForm

    #model = Person

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return  super(PersonCreate, self).form_valid(form)
        

            

class PersonUpdate(LoginRequiredMixin, UpdateView):
    model = Person
    template_name = "apli/person_form.html"
    form_class = PersonForm

    def form_valid(self, form):
        form.instance.last_edited_by = self.request.user
        return  super(PersonUpdate, self).form_valid(form)
       

class PersonDelete(LoginRequiredMixin, DeleteView):
    model = Person
    success_url = reverse_lazy('person_index')   



 ############################################################
#   PROJECT: Index, detail, create, update, delete.

@login_required(login_url='/register/login/')
def project_index(request):
    all_projects = Project.objects.all()
   

    return render(request, 'apli/menu/project/project_index.html', {'all_projects': all_projects})
    
@login_required(login_url='/register/login/')   
def project_detail(request, pk):
    project = get_object_or_404(Project, id=pk)
    all_persons = project.assignment_set.all()
    all_attachments = project.attachment_set.all()
    all_costs = project.cost_set.all()
    return render(request, 'apli/menu/project/project_detail.html', {'project': project, 'all_persons': all_persons, 'all_attachments': all_attachments, 'all_costs': all_costs})

class ProjectCreate(LoginRequiredMixin, CreateView):
    
    template_name = "apli/project_form.html"
    form_class = ProjectForm


    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return  super(ProjectCreate, self).form_valid(form)
    
   
class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = "apli/project_form.html"
    form_class = ProjectForm

    def form_valid(self, form):
        form.instance.last_edited_by = self.request.user
        return  super(ProjectUpdate, self).form_valid(form)

class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('project_index')
