from django.contrib.syndication.views import Feed
from django.conf.urls.defaults import patterns, url

from django.shortcuts import get_object_or_404
from blog.models import Posts

class LastPosts(Feed):
    title       = "Python Turkiye - Blog"
    link        = "/"
    description = "Python Turkiye.Turkce Python Programlama Dili Kaynaklari ve Dersleri"

    def items(self):
        return Posts.objects.order_by("-created").filter(isonline=True)[:5]

    def item_title(self, item):
        return item.sef_title

    def item_description(self, item):
        return item.hom_content

    def item_pubdate(self, item):
        return item.created

RSS_URLS = patterns('',
    url(r'^rss/$', LastPosts()),
)