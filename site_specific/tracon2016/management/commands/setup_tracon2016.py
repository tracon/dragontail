# encoding: utf-8

from __future__ import print_function, unicode_literals

from datetime import datetime, timedelta, date

from django.core.files import File
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils.timezone import now

from wagtail.wagtailcore.models import Site

from dragontail.content.models import BasicPage, TemplateSettings


class Command(BaseCommand):
    args = ''
    help = 'Setup example content'

    def add_arguments(self, parser):
        parser.add_argument('hostname', type=str)

    def handle(self, *args, **options):
        Setup(hostname=options['hostname']).setup()


class Setup(object):
    def __init__(self, hostname):
        self.hostname = hostname

    def setup(self):
        print('NOTE: Setting up Tracon (2016) site at {hostname}'.format(hostname=self.hostname))
        self.setup_content()
        # self.setup_ads()
        # self.setup_blog()

    def setup_content(self):
        t = now()

        is_default_site = not Site.objects.exists()

        self.root_page, unused = BasicPage.objects.get_or_create(
            slug='index',
            defaults=dict(
                title='Tracon Tampere-talossa 3.–4. syyskuuta 2016',
                depth=0
            )
        )

        self.site, unused = Site.objects.get_or_create(hostname=self.hostname, defaults=dict(
            is_default_site=is_default_site,
            root_page=self.root_page,
        ))

        self.template_settings, unused = TemplateSettings.objects.get_or_create(
            site=self.site,
            defaults=dict(
                base_template='tracon11_base.jade',
                basic_page_template='tracon11_page.jade',
                blog_index_template='tracon11_blog_index.jade',
                blog_post_template='tracon11_blog_post.jade',
            )
        )

        return

        ordering = 0
        for page_slug, page_title, child_pages in [
            ('front-page', 'Tracon Tampere-talossa 3.–4. syyskuuta 2016', []),
            ('blog', 'Ajankohtaista', []), # pseudo page for menu, actually taken over by blog
            ('tapahtuma', 'Tapahtuma', [
                ('tyovoima', 'Vänkäriksi'),
                ('jarjestyssaannot', 'Järjestyssäännöt'),
                ('tapahtumapaikka', 'Tapahtumapaikka'),
            ]),
            ('ohjelma', 'Ohjelma', [
                ('ohjelmanjarjestajaksi', 'Ohjelmanjärjestäjäksi'),
            ]),
            ('liput', 'Liput', []),
            ('yhteys', 'Ota yhteyttä!', [
                ('conitea', 'Järjestäjät'),
                ('media', 'Tiedotusvälineille'),
                ('sponsorit', 'Yhteistyökumppaneille'),
            ])
        ]:
            ordering += 10

            parent_page, unused = Page.objects.get_or_create(
                site=self.site,
                parent=None,
                slug=page_slug,
                defaults=dict(
                    title=page_title,
                    body='Placeholder for {slug}'.format(slug=page_slug),
                    public_from=t,
                    visible_from=t,
                    order=ordering,
                )
            )

            # v2
            child_ordering = 0
            for child_slug, child_title in child_pages:
                child_ordering += 10

                child_page, unused = Page.objects.get_or_create(
                    site=self.site,
                    parent=parent_page,
                    slug=child_slug,
                    defaults=dict(
                        title=child_title,
                        body='Placeholder for {slug}'.format(slug=child_slug),
                        public_from=t,
                        visible_from=t,
                        order=child_ordering,
                    )
                )

                # v2
                if child_page.order == 0:
                    child_page.order = child_ordering
                    child_page.save()

        front_page = Page.objects.get(site=self.site, slug='front-page')
        if not front_page.override_menu_text:
            front_page.override_menu_text = 'Etusivu'
        # v11
        if not front_page.override_page_template:
            front_page.override_page_template = 'tracon11_front_page.jade'
        if not front_page.page_controller_code or front_page.page_controller_code == 'events.tracommon.views:front_page_controller':
            front_page.page_controller_code = 'site_specific.tracommon.views:front_page_controller'
        front_page.save()

        for path, target in [
            ('admin', '/admin/'),
        ]:
            redirect, unused = Redirect.objects.get_or_create(
                site=self.site,
                path=path,
                defaults=dict(
                    target=target
                ),
            )

    def setup_ads(self):
        for banner_title, banner_url, banner_path in [
            ('Säätöyhteisö B2 ry', 'http://b2.fi', 'site_specific/tracon11/static/tracon11/img/b2-saatoa2008-wh-200.png'),
        ]:
            try:
                Banner.objects.get(sites=self.site, url=banner_url)
            except Banner.DoesNotExist:
                with open(banner_path, 'rb') as banner_file:
                    banner = Banner(
                        title=banner_title,
                        url=banner_url,
                        image_file=File(banner_file),
                    )

                    banner.save()

                    banner.sites = [self.site,]
                    banner.save()

    def setup_blog(self):
        """
        Set up a stub of the blog.tracon.fi site required by the front page blog box.
        """
        blog_site, unused = Site.objects.get_or_create(hostname='blog.tracon.fi', defaults=dict(
            name='Traconin blogi'
        ))
        blog_site_settings, unused = SiteSettings.objects.get_or_create(site=blog_site, defaults=dict(
            base_template='tracon11_base.jade',
            page_template='tracon11_page.jade',
            blog_index_template='tracon11_blog_index.jade',
            blog_post_template='tracon11_blog_post.jade',
        ))

        for category_slug, category_title in [
            ('conzine', 'Conzine'),
            ('palaute', 'Palaute'),
            ('jarjestaminen', 'Traconin järjestäminen'),
        ]:
            BlogCategory.objects.get_or_create(
                site=blog_site,
                slug=category_slug,
                defaults=dict(
                    title=category_title,
                )
            )

