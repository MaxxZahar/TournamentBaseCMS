from django.forms import ModelForm
from ..models import TableModel


class TableForm(ModelForm):
    class Meta:
        model = TableModel
        fields = '__all__'
