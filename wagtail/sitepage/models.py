from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

import home

class SitePage(Page):
    page_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        help_text='Primary Page Image'
    )
    page_content = RichTextField(
        blank=True,
        features=[
            "bold",
            "italic",
            "ol",
            "ul",
            "hr",
            "link",
            "blockquote",
        ]
    )
    # FIX THIS!!!!!!! - CODE TO INCLUDE HOME PAGE IMAGES
    # def get_context(self, request):
    #     context = super(home.objects(), self).get_context(request)
    #     context['left_image'] = home.top_image
    #     context['right_image'] = home.second_image
    #     return context

    class Meta:
        verbose_name = "Site page"
        verbose_name_plural = "Site pages"

    subpage_types = []
