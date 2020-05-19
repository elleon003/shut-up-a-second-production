from django.db import models

from wagtail.contrib.settings.models import BaseSetting, register_setting

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


@register_setting
class FooterSettings(BaseSetting):
    left_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        help_text='Left Footer Image'
    )
    right_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        help_text='Right Footer Image'
    )
    newsletter_title = models.CharField(
        max_length=140,
        blank=False,
        null=False,
        default='Sign up for my newsletter',
        help_text='Heading for newsletter footer'
    )
    newsletter_text = models.TextField(
        max_length=500,
        blank=True,
        null=False, 
        help_text='Text for newsletter footer'
    )
    newsletter_button_text = models.TextField(
        max_length=50,
        blank=False,
        null=False,
        default="Sign Me Up!",

    )

    panels =[
        ImageChooserPanel("left_image"),
        ImageChooserPanel("right_image"),
        FieldPanel("newsletter_title"),
        FieldPanel("newsletter_text"),
        FieldPanel("newsletter_button_text"),
    ]
