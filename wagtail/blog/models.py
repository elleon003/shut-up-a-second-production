from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class BlogListingPage(Page):
    pass
    # TODO 

class BlogPost(Page):
    post_date = models.DateField(
        "Post Date")
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('post_date'),
        FieldPanel('body'),
    ]

    subpage_types = []
