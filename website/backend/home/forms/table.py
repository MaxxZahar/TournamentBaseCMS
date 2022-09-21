from django.forms import ModelForm
from ..models import TableModel
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class TableForm(ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    class Meta:
        model = TableModel
        fields = '__all__'
