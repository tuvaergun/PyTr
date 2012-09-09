from django.contrib.syndication.views import Feed
from django.conf.urls.defaults import patterns, url

from django.shortcuts import get_object_or_404
from sources.models import Sources

class LastSources(Feed):
    title       = "Python Turkiye - Kaynaklar"
    link        = "/"
    description = "Python Turkiye.Turkce Python Programlama Dili Kaynaklari ve Dersleri"

    def items(self):
        return Sources.objects.order_by("-created").filter(isonline=True)[:5]

    def item_title(self, item):
        return item.sef_title

    def item_description(self, item):
        return item.description

    def item_pubdate(self, item):
        return item.created

SOURCES_RSS_URLS = patterns('',
    url(r'^rss/sources$', LastSources()),
)