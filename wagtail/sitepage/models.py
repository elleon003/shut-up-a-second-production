from django.db import models

from wagtail.core.models import Page

class SitePage(Page):

    class Meta:
        verbose_name = "Site page"
        verbose_name_plural = "Site pages"
