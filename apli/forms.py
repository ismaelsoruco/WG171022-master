from django import forms
from .models import Person, Project, Cost, Attachment, Horaire, Assignment, Time



YEARS = [x for x in range(1980,2031)]
YEAR_DATE = [x for x in range(2015,2031)]


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            "name",
            "name_short",
            "phone",
            "email",
            "IBAN",
            "birthday",
            "company",
            "company_short",
            # "country",
            # "city",
            # "zip_code",
            # "address",
            # "comment",
            # "agent",
            # "agent_short",
            "client",
             "model",
             "photographe",
             "make_up",
             "styling",
             "other",
             "comment_other",
            # "sedcard_cost",
            # "sedcard_payed",
            # "bank_account",
            # "website"
        ]
            

class ProjectForm(forms.ModelForm):



    start               = forms.DateField(widget=forms.SelectDateWidget(years=YEAR_DATE), label="Stardatum")
    finish              = forms.DateField(initial="2010-11-20", widget=forms.SelectDateWidget(years=YEAR_DATE), label="Enddatum")
    name                = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'special'}), initial="", label="Projektname")
    comment             = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 1, "cols": 22}), label="Komment")
    other_description   = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 1, "cols": 22}), label="Anderer Beschreibung")
    comment_address     = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 1, "cols": 22}), label="Adresskomment")

    class Meta: 
        model = Project
        fields = [
            'name',
            'client',
            'start',
            'finish',
            'user',
            'comment',
            'sort',
            'all_day',
            'half_day',
            'half_day_price_pro',
            'all_day_price_pro',
            'over_price_pro',
            'all_in_price_pro',
            'half_day_price_semipro',
            'all_day_price_semipro',
            'over_price_semipro',
            'all_in_price_semipro',
            'country',
            'city',
            'zip_code',
            'address',
            'comment_address',
            'honorary_base',
            'honorary_plus',
            'quantity_models_honorary_plus',
            'ms_price',
            'ms_hours',
            'requirement_price',
            'requirement_hours',
            'requisiten_price_for_each_model',
            'other_title',
            'other_description',
            'other_price',
            'other_hours',
            'photo_price',
            'photo_hours',
            'tax',
            'statut'
        ]

class CostForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget(years=YEAR_DATE), label="Datum")
    comment = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 1, "cols": 22}), label="Komment")



    class Meta: 
        model = Cost
        fields = [
            'user',
             'project',
             'comment',
             'date',
             'amount',
             'title',
             'statut'
        ]

class AttachmentForm(forms.ModelForm):
    send_date = forms.DateField(widget=forms.SelectDateWidget(years=YEAR_DATE), label="Senddatum")
    answer_date = forms.DateField(widget=forms.SelectDateWidget(years=YEAR_DATE), label="Antwortdatum")
    comment_WG = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 1, "cols": 22}), label="Komment wg")
    comment_client = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 1, "cols": 22}), label="Komment kunde")


    class Meta: 
        model = Attachment
        fields = [
            'sort',
             'file',
             'send_date',
             'answer_date',
             'statut',
             'comment_WG',
             'comment_client',
             'project',
             'person'
        ]

class HoraireForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget(years=YEAR_DATE), label="Datum")
    start_time = forms.TimeField(widget=forms.TimeInput(format='%I:%M %p',), label="Startdatum")
    finish_time = forms.TimeField(widget=forms.TimeInput(format='%I:%M %p',), help_text="Enter a date between now and 4 weeks (default 3).", label="Endedatum")

    class Meta: 
        model = Horaire
        fields = [
             'assignment',
             'date',
             'start_time', 
             'finish_time'
        ]

class AssignmentForm(forms.ModelForm):

    def bla (request):
        project = get_object_or_404(Project, id=pk)
        projecto = self.request.project
        
    comment_WG = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 1, "cols": 22}), label="Komment")
    send_date = forms.DateField(widget=forms.SelectDateWidget(years=YEAR_DATE), label="Senddatum")
    payment_date = forms.DateField(widget=forms.SelectDateWidget(years=YEAR_DATE), label="Bezhaldatum")
   
    class Meta: 
        model = Assignment
        fields = [
            'project',
            'person',
            'model_type',
            'travel_cost',
            'hotel_cost',
            'other_cost',
            'comment_WG',
            'statut',
            'send_date',
            'payment_date',
            'total_price'
        ]

class TimeForm(forms.ModelForm):
    start_time = forms.TimeField(widget=forms.TimeInput(format='%I:%M %p',), label="Startdatum")
    finish_time = forms.TimeField(widget=forms.TimeInput(format='%I:%M %p',), label="Enddatum")
    date = forms.DateField(widget=forms.SelectDateWidget(years=YEAR_DATE), label="Datum")
    comment = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 1, "cols": 22}), label="Komment")

    class Meta: 
        model = Time
        fields = [
            'title',
             'user',
             'comment',
             'date',
             'start_time',
             'finish_time',
             'project'
        ]