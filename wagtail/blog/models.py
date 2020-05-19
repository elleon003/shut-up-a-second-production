from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

import home

class BlogListingPage(Page):
    parent_page_types = ["home.HomePage"]
    subpage_types = ["blog.BlogPost"]
    max_count = 1

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        all_posts = BlogPost.objects.live().order_by('-first_published_at')

        paginator = Paginator(all_posts, 4)

        page = request.GET.get("page")
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        
        context["posts"] = posts
        return context


class BlogPost(Page):
    post_date = models.DateField(
        "Post Date")
    body = RichTextField(
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
    blog_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        help_text='Primary Post Image'
    )

    def prev_post(self):
        prev = self.get_prev_sibling()
        if prev and prev.live:
            return prev
    
    def next_post(self):
        next = self.get_next_sibling()
        if next and next.live:
            return next

    parent_page_types = ["blog.BlogListingPage"]
    subpage_types = []

    content_panels = Page.content_panels + [
        FieldPanel('post_date'),
        FieldPanel('body'),
        ImageChooserPanel('blog_image'),
    ]
    

