# encoding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class TemplateSettings(BaseSetting):
    base_template = models.CharField(
        max_length=127,
        verbose_name=_('Base template'),
        help_text=_('Defines the basic layout of the site. A template with this name must be present in the source code.'),
    )

    basic_page_template = models.CharField(
        max_length=127,
        verbose_name=_('Basic page template'),
        help_text=_('This template is used to render basic content pages. A template with this name must be present in the source code.'),
    )

    blog_index_template = models.CharField(
        max_length=127,
        verbose_name=_('Blog index template'),
        help_text='This template is used to render the blog index. A template with this name must be present in the source code.',
    )

    blog_post_template = models.CharField(
        max_length=127,
        verbose_name=_('Blog post template'),
        help_text='This template is used to render a single blog post. A template with this name must be present in the source code.',
    )