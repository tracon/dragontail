  # encoding: utf-8

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock


class BasicPage(Page):
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    def get_template(self, request, *args, **kwargs):
        from .templatesettings import TemplateSettings

        template_settings = TemplateSettings.for_site(request.site)

        return template_settings.basic_page_template