from django.db import models
from garpix_page.models import BasePage


class HomePage(BasePage):
    template = "pages/home.html"

    def get_context(self, request=None, *args, **kwargs):
        from ..forms import TableForm
        context = super().get_context(request, *args, **kwargs)
        if request.method == 'POST':
            form = TableForm(request.POST, request.FILES)
            print('Received')
            print(request.FILES)
            file = request.FILES['table'].readlines()
            print(file)
            get_data_from_request(file)
            if form.is_valid():
                form.save()
                print('Valid')
                context.update({
                    'message': 'Сообщение успешно отправлено',
                })
            else:
                print(form.errors.as_data())
            context.update({
                'form': form,
            })
        return context

    class Meta:
        verbose_name = "Главная"
        verbose_name_plural = "Главная"
        ordering = ("-created_at",)


def get_data_from_request(file):
    table = []
    for line in file:
        table.append(line.decode('UTF-8'))
    table_header = table[0].strip()
    left_comma_index = table_header.index(',')
    right_comma_index = table_header.rindex(',')
    name = table_header[1:left_comma_index].strip()
    location = table_header[left_comma_index + 1:right_comma_index].strip()
    date = table_header[right_comma_index + 1:-1].strip()
    if len(date) == 10:
        start_date = date
        finish_date = date
    elif len(date) == 23:
        start_date = date[:10]
        finish_date = date[13:]
    elif len(date) == 21:
        start_date = date[:10]
        finish_date = date[11:]
    else:
        raise ValueError('Wrong date format')
    print(name, location, start_date, finish_date)
