import django_tables2 as tables
from .models import Person




class PersonTable(tables.Table):#name
	Edit = tables.TemplateColumn('<a href="{% url \'person_detail\' record.id %}">Edit</a>', orderable=False)
	phone = tables.Column(orderable=False)
	selection = tables.CheckBoxColumn(accessor='pk', orderable=False)


	class Meta:
		model = Person
		email = tables.EmailColumn()
		name = tables.URLColumn()
		order_by = '-name'
		name = tables.Column(footer='Total:')



		template = 'django_tables2/bootstrap.html'
		fields = [
            'name',
            'company',
            'email',
            'phone',
        ]