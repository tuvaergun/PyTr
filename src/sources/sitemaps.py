from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.conf.urls.defaults import patterns, url

from sources.models import Sources, Categories

posts_dict = {
    'queryset': Sources.objects.order_by("-created").filter(isonline=True),
    'date_field': 'created',
    }
categories_dict = {
    'queryset': Categories.objects.all(),
    }

sitemaps = {
    'posts': GenericSitemap(posts_dict, priority=0.5),
    'categories': GenericSitemap(categories_dict, priority=1),
    }

SOURCES_SITEMAPS_URLS = patterns('django.contrib.sitemaps.views',
    url(r'^sitemap-sources\.xml$', 'sitemap', {'sitemaps': sitemaps}),
)