from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.conf import settings



class Person(models.Model):
    name            = models.CharField(max_length=20, verbose_name="Name", default="")
    name_short      = models.CharField(max_length=100, blank=True, verbose_name="Kontaktkursname")
    company         = models.CharField(max_length=200, blank=True, verbose_name="Firma")
    company_short   = models.CharField(max_length=100, blank=True, verbose_name="Firmakursname")
    country         = models.CharField(max_length=50, blank=True, verbose_name="Land")
    city            = models.CharField(max_length=50, blank=True, verbose_name="Stadt")
    zip_code        = models.CharField(max_length=15, blank=True, verbose_name="code")
    address         = models.CharField(max_length=100, blank=True, verbose_name="Adresse")
    email           = models.EmailField(verbose_name="E-mail")
    phone_regex     = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone           = models.CharField(validators=[phone_regex], max_length=15, verbose_name="Phone")
    comment         = models.TextField(max_length=500, blank=True, verbose_name="Kommentar")
    birthday        = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Geburstag", help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    agent           = models.CharField(max_length=200, blank=True, verbose_name="Agent")
    agent_short     = models.CharField(max_length=100, blank=True, verbose_name="Kurs Agentname")
    client          = models.BooleanField(default=False, verbose_name="Kunde")
    model           = models.BooleanField(default=False, verbose_name="Modell")
    photographe     = models.BooleanField(default=False, verbose_name="Photograph")
    make_up         = models.BooleanField(default=False, verbose_name="Make-up")
    styling         = models.BooleanField(default=False, verbose_name="Styling")
    other           = models.BooleanField(default=False, verbose_name="Andere")
    comment_other   = models.CharField(max_length=200, blank=True, verbose_name="Kommentar von andere")
    sedcard_cost    = models.IntegerField(null=True, blank=True, verbose_name="Kost")
    sedcard_payed   = models.IntegerField(null=True, blank=True, verbose_name="Sedcard")
    sedcard_statut  = models.BooleanField(default=False, verbose_name="Sedcard Status")
    bank_regex      = RegexValidator(regex=r'^DE\d{2}\s?([0-9a-zA-Z]{4}\s?){4}[0-9a-zA-Z]{2}$', message="Bank account must be entered in the format: 'DE12 3456 7890 1234 5678 90'. Up to 27 digits allowed.")
    bank_account    = models.CharField(validators=[bank_regex], max_length=27, verbose_name="Konto")
    IBAN            = models.CharField(max_length=200, blank=True, verbose_name="IBAN")
    website         = models.URLField(max_length=200, blank=True, verbose_name="website")
    slug            = models.SlugField(null=True, blank=True)
    last_edited_by  = models.ForeignKey(User, null=True, blank=True, related_name='person_edit')
    added_by        = models.ForeignKey(User, null=True, blank=True, related_name='person_add')

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'
        ordering = ["-id"]

    def get_absolute_url(self):
        return reverse('person_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
        

    # def clean_website(self, *args, **kwargs)
    #     website = self.cleaned_data.get("Website")
    #     print(website)
    #     raise forms.

    @property
    def title(self):
        return self.name

    def rl_pre_save_receiver(sender,instance, *args, **kwargs):
        if not instance.slug:
            instance.name ="blabla"
            instance.slug = unique_slug_generator(instance)

    # def rl_post_save_receiver(sender,instance, *args, **kwargs):
    #     if not instance.slug:
    #         instance.slug = unique_slug_generator(instance)
    #         instance.save()

    #pre_save.connect(rl_pre_save_receiver, sender=Person)

    # post_save.connect(rl_post_save_receiver, sender=Person)



class Project(models.Model):
    name                            = models.CharField(max_length=200)
    client                          = models.ForeignKey(Person, on_delete=models.CASCADE)
    start                           = models.DateField()
    finish                          = models.DateField()
    user                            = models.ForeignKey(User, on_delete=models.CASCADE)
    comment                         = models.CharField(max_length=500, blank=True)
    sort                            = models.CharField(max_length=8, choices=(('Angebot', 'angebot'), ('Auftrag', 'aufttrag'), ('Job', 'job'),), default='Angebot')
    all_day                         = models.IntegerField(null=True, blank=True)
    half_day                        = models.IntegerField(null=True, blank=True)
    half_day_price_pro              = models.IntegerField(null=True, blank=True)
    all_day_price_pro               = models.IntegerField(null=True, blank=True)
    over_price_pro                  = models.IntegerField(null=True, blank=True)
    all_in_price_pro                = models.IntegerField(null=True, blank=True)
    half_day_price_semipro          = models.IntegerField(null=True, blank=True)
    all_day_price_semipro           = models.IntegerField(null=True, blank=True)
    over_price_semipro              = models.IntegerField(null=True, blank=True)
    all_in_price_semipro            = models.IntegerField(null=True, blank=True)
    country                         = models.CharField(max_length=50, blank=True)
    city                            = models.CharField(max_length=50, blank=True)
    zip_code                        = models.CharField(max_length=15, blank=True)
    address                         = models.CharField(max_length=100, blank=True)
    comment_address                 = models.CharField(max_length=500, blank=True)
    honorary_base                   = models.IntegerField(null=True, blank=True)
    honorary_plus                   = models.IntegerField(null=True, blank=True)
    quantity_models_honorary_plus   = models.IntegerField(null=True, blank=True)
    ms_price                        = models.IntegerField(null=True, blank=True)
    ms_hours                        = models.IntegerField(null=True, blank=True)
    requirement_price               = models.IntegerField(null=True, blank=True)
    requirement_hours               = models.IntegerField(null=True, blank=True)
    requisiten_price_for_each_model = models.IntegerField(null=True, blank=True)
    other_title                     = models.CharField(max_length=50, blank=True)
    other_description               = models.CharField(max_length=200, blank=True)
    other_price                     = models.IntegerField(null=True, blank=True)
    other_hours                     = models.IntegerField(null=True, blank=True)
    photo_price                     = models.IntegerField(null=True, blank=True)
    photo_hours                     = models.IntegerField(null=True, blank=True)
    total_price                     = models.IntegerField(null=True, blank=True)
    tax                             = models.IntegerField(default=19)
    statut                          = models.CharField(max_length=9, choices=(('Draft', 'draft'), ('yyy', 'active'), ('xxx', 'facture_sent'), ('bezhal', 'payed'), ('Absagen', 'canceled'),), default='Draft')
    last_edited_by                  = models.ForeignKey(User, null=True, blank=True, related_name='person_edit1')
    added_by                        = models.ForeignKey(User, null=True, blank=True, related_name='person_add1')

    class Meta:
        verbose_name        = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ["name"]
        
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
    


class Attachment(models.Model):
    sort            = models.CharField(max_length=9, choices=(('angebot', 'angebot'), ('aufttrag', 'aufttrag'), ('job', 'job'), ('facture_client', 'facture_client'), ('facture_person', 'facture_person'),), default='angebot')
    file            = models.FileField()
    send_date       = models.DateField()
    answer_date     = models.DateField(null=True, blank=True)
    statut          = models.CharField(max_length=14, choices=(('waiting answer', 'waiting answer'), ('accepted', 'accepted'), ('rejected', 'rejected'),), default='waiting answer')
    comment_WG      = models.CharField(max_length=500, blank=True)
    comment_client  = models.CharField(max_length=500, blank=True)
    project         = models.ForeignKey(Project, on_delete=models.CASCADE)
    person          = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
    last_edited_by  = models.ForeignKey(User, null=True, blank=True, related_name='person_edit2')
    added_by        = models.ForeignKey(User, null=True, blank=True, related_name='person_add2')

    class Meta:
        verbose_name        = 'Attachment'
        verbose_name_plural = 'Attachments'



    def __str__(self):
        return self.sort


class Assignment(models.Model):
    project             = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)
    person              = models.ForeignKey(Person, on_delete=models.CASCADE)
    model_type          = models.CharField(max_length=14, choices=(('pro', 'pro'), ('semipro', 'semipro'),), default='pro')
    travel_cost         = models.IntegerField(null=True, blank=True)
    hotel_cost          = models.IntegerField(null=True, blank=True)
    other_cost          = models.IntegerField(null=True, blank=True)
    comment_WG          = models.CharField(max_length=500, blank=True)
    comment_model       = models.CharField(max_length=500, blank=True)
    statut              = models.CharField(max_length=14, choices=(('created', 'created'), ('waiting answer', 'waiting answer'), ('confirmed', 'confirmed'), ('not possible', 'not possible'), ('realized', 'realized'), ('acquitted', 'acquitted'),), default='created')
    send_date           = models.DateField(null=True, blank=True)
    confirmation_date   = models.DateField(null=True, blank=True)
    payment_date        = models.DateField(null=True, blank=True)
    total_price         = models.IntegerField(null=True, blank=True)
    last_edited_by      = models.ForeignKey(User, null=True, blank=True, related_name='person_edit3')
    added_by            = models.ForeignKey(User, null=True, blank=True, related_name='person_add3')

    class Meta:
        verbose_name        = 'Assignment'
        verbose_name_plural = 'Assignments'

    def __str__(self):
        return self.person.name + ' - ' + self.project.name

    def get_absolute_url(self):
        return reverse('assignment_detail', kwargs={'pk': self.pk})


class Horaire(models.Model):
    assignment          = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    date                = models.DateField()
    start_time          = models.TimeField()
    finish_time         = models.TimeField()
    start_time_real     = models.TimeField(null=True, blank=True)
    finish_time_real    = models.TimeField(null=True, blank=True)
    last_edited_by      = models.ForeignKey(User, null=True, blank=True, related_name='person_edit4')
    added_by            = models.ForeignKey(User, null=True, blank=True, related_name='person_add4')

    class Meta:
        verbose_name        = 'Horaire'
        verbose_name_plural = 'Horaires'


    def get_absolute_url(self):
        return reverse('assignment_detail', kwargs={'pk': self.pk})


class Cost(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    project             = models.ForeignKey(Project, on_delete=models.CASCADE)
    comment             = models.CharField(max_length=500, blank=True)
    date                = models.DateField()
    amount              = models.IntegerField()
    title               = models.CharField(max_length=100)
    statut              = models.CharField(max_length=14, choices=(('planned', 'planned'), ('complete', 'complete'),), default='planned')
    last_edited_by      = models.ForeignKey(User, null=True, blank=True, related_name='person_edit5')
    added_by            = models.ForeignKey(User, null=True, blank=True, related_name='person_add5')

    class Meta:
        verbose_name        = 'Cost'
        verbose_name_plural = 'Costs'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cost_detail', kwargs={'pk': self.pk})


class Time(models.Model):
    title           = models.CharField(max_length=100)
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    comment         = models.CharField(max_length=500, blank=True)
    date            = models.DateField()
    start_time      = models.TimeField()
    finish_time     = models.TimeField()
    project         = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    last_edited_by  = models.ForeignKey(User, null=True, blank=True, related_name='person_edit6')
    added_by        = models.ForeignKey(User, null=True, blank=True, related_name='person_add6')

    class Meta:
        verbose_name        = 'Time'
        verbose_name_plural = 'Times'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('time_detail', kwargs={'pk': self.pk})
