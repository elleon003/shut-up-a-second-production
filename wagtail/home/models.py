from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from blog.models import BlogPost


class HomePage(Page):
    # First Row content
    top_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        help_text='The top, primary image'
    )
    about_header = models.CharField(
        blank=False,
        null=True,
        help_text='Header for the about page teaser',
        max_length=140,
    )
    lead_text = models.CharField(
        blank=False,
        null=True,
        max_length=500, 
        help_text='Intro to about section text',
    )
    linked_page = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name="+",
        help_text='Select a page to link to',
        on_delete=models.SET_NULL,
    )
    linked_page_text = models.CharField(
        max_length=50,
        default='Read More',
        blank=False,
        help_text='Link text',
    )

    # TODO - second row content
        # Img Uploader
    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['latest_post'] = BlogPost.objects.live().last()
        return context

        # Most Recent Post Heading
        # Most Recent Post Blurb
        # Link to Post

    # TODO Third Row - Contact info

    parent_page_types = []
    max_count = 1
    subpage_types = ["blog.BlogListingPage", "sitepage.SitePage",]


    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                ImageChooserPanel("top_image"),
                FieldPanel("about_header"),
                FieldPanel("lead_text"),
                PageChooserPanel("linked_page"),
                FieldPanel("linked_page_text"),
            ],
            heading="First Row",
            classname="collapsible",
        )
    ]

    
