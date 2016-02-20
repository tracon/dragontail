# from .models import Banner


def ads_context(request):
    return dict(
        banners=[], # XXX Banner.objects.filter(sites=request.site, active=True).order_by('?')
    )
