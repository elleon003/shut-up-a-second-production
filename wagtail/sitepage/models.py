from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


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
    newsletter_title = models.CharField(
        max_length=140,
        blank=False,
        null=False,
        default='Sign up for my newsletter'
    )
    newsletter_text = models.TextField(
        max_length=500,
        blank=True,
        null=False,
    )

    class Meta:
        verbose_name = "Site page"
        verbose_name_plural = "Site pages"
    
    content_panels = Page.content_panels + [
        ImageChooserPanel("page_image"),
        FieldPanel("page_content"),
        FieldPanel("newsletter_title"),
        FieldPanel("newsletter_text"),
    ]
    
    subpage_types = []
