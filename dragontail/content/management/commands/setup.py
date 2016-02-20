# encoding: utf-8

from django.core.management import call_command
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.conf import settings

from wagtail.wagtailcore.models import Page


class Command(BaseCommand):
    args = ''
    help = 'Setup all the things'

    def handle(self, *args, **options):
        management_commands = [
            (('collectstatic',), dict(interactive=False)),
            (('migrate',), dict()),
        ]

        if 'kompassi_oauth2' in settings.INSTALLED_APPS:
            management_commands.append((('setup_kompassi_oauth2',), dict()))

        for pargs, opts in management_commands:
            call_command(*pargs, **opts)

        Page.objects.filter(title='Welcome to your new Wagtail site!').delete()

        if settings.DEBUG:
            user, created = User.objects.get_or_create(
                username='mahti',
                first_name='Markku',
                last_name='Mahtinen',
                is_staff=True,
                is_superuser=True,
            )

            if created:
                user.set_password('mahti')
                user.save()
                print('WARNING: Creating superuser "mahti" with password "mahti"')
