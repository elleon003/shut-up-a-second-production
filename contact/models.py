from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.core.fields import RichTextField

from modelcluster.models import ParentalKey

from wagtailcaptcha.models import WagtailCaptchaEmailForm
from wagtailcaptcha.forms import WagtailCaptchaFormBuilder


# Admin choices for the class below
FORM_FIELD_CHOICES = (
    ('singleline', _('Single line text')),
    ('multiline', _('Multi-line text')),
    ('email', _('Email')),
    ('hidden', _('Hidden field')),
)


# Limit the field choices in the admin
class CustomAbstractFormField(AbstractFormField):
    field_type = models.CharField(
        verbose_name="Field Type",
        max_length=16,
        choices=FORM_FIELD_CHOICES,
    )
    class Meta:
        abstract = True
        ordering = ["sort_order"]


class FormField(AbstractFormField):
    page = ParentalKey(
        "ContactPage",
        on_delete=models.CASCADE,
        related_name = 'form_fields'
    )


class ContactPage(WagtailCaptchaEmailForm):
    intro = RichTextField(
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
    thank_you_text = RichTextField(
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

    content_panels = AbstractEmailForm.content_panels +[
        FieldPanel("intro"),
        InlinePanel("form_fields", label='Form Fields'),
        FieldPanel("thank_you_text"),
        FieldPanel("from_address"),
        FieldPanel("to_address"),
        FieldPanel("subject"),
    ]

    parent_page_types = ["home.HomePage"]
    subpage_types = []
    max_count = 1
