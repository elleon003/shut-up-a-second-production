from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class BlogListingPage(Page):
    parent_page_types = ["home.HomePage"]
    subpage_types = ["blog.BlogPost"]
    max_count = 1

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['posts'] = BlogPost.objects.live().order_by('-first_published_at')
        return context


class BlogPost(Page):
    post_date = models.DateField(
        "Post Date")
    body = RichTextField(blank=True)

    def prev_post(self):
        if self.get_prev_sibling():
            return self.get_prev_sibling()
    
    def next_post(self):
        if self.get_next_sibling():
            return self.get_next_sibling()

    content_panels = Page.content_panels + [
        FieldPanel('post_date'),
        FieldPanel('body'),
    ]
    parent_page_types = ["blog.BlogListingPage"]
    subpage_types = []

