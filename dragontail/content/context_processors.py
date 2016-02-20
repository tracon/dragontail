from django.conf import settings


def content_context(request):
    app_name = (
        'Dragontail CMS Enterprise Edition'
        if 'kompassi_oauth2' in settings.INSTALLED_APPS
        else 'Dragontail CMS Standard Edition'
    )

    return dict(
        menu=[], # XXX
        settings=settings,
        dragontail_app_name=app_name,
        dragontail_footer=u"<a href='https://github.com/tracon/dragontail' target='_blank'>{app_name}"
            u"</a> © 2016 <a href='https://github.com/tracon/dragontail/blob/master/LICENSE.md'>"
            "Santtu Pajukanta</a>.".format(app_name=app_name)
    )