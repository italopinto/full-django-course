from django.forms import ModelForm
from .models import Client, ID


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'last_name', 'age', 'salary', 'email', 'photos', 'dt_birth', 'doc_id']


class IdForm(ModelForm):
    class Meta:
        model = ID
        fields = ['number']
