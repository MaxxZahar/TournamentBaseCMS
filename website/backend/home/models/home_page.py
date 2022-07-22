from django.db import models
from garpix_page.models import BasePage


class HomePage(BasePage):
    template = "pages/home.html"

    class Meta:
        verbose_name = "Главная"
        verbose_name_plural = "Главная"
        ordering = ("-created_at",)
