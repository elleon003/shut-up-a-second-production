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

    # Second row content
    second_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        help_text='The top, primary image'
    )
    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['latest_post'] = BlogPost.objects.live().last()
        return context

    # Third Row - Contact info
    section_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        default='Contact Me'
    )
    section_text = models.TextField(
        max_length=500,
        blank=True,
        null=False,
    )
    section_button_text = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        default="Contact Me",
    )
    section_button = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name="+",
        help_text='Select a page to link to',
        on_delete=models.SET_NULL,
    )
    facebook_link = models.URLField(
        "Facebook link", 
        blank=True,
        help_text="Enter your full Facebook URL"
    )
    twitter_link = models.URLField(
        "Twitter link",
        blank=True,
        help_text="Enter your full Twitter URL"
    )

    parent_page_types = []
    max_count = 1
    subpage_types = ["blog.BlogListingPage", "sitepage.SitePage", "contact.ContactPage"]

    content_panels = Page.content_panels + [
        # First Row Content
        MultiFieldPanel(
            [
                ImageChooserPanel("top_image"),
                FieldPanel("about_header"),
                FieldPanel("lead_text"),
                PageChooserPanel("linked_page"),
                FieldPanel("linked_page_text"),
            ],
            heading="First Row Content",
            classname="collapsible collapsed",
        ),
        # Second Row Content
        MultiFieldPanel(
            [
                ImageChooserPanel('second_image'),
            ],
            heading="Second Row Content",
            classname="collapsible collapsed",
        ),
        # Third Row Content
        MultiFieldPanel(
            [
                FieldPanel("section_title"),
                FieldPanel("section_text"),
                FieldPanel("section_button_text"),
                PageChooserPanel("section_button"),
                FieldPanel("facebook_link"),
                FieldPanel("twitter_link"),
            ],
            heading="Third Row Content",
            classname="collapsible collapsed",
        )
        
    ]





