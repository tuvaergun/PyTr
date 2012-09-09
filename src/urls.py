from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from settings import MEDIA_ROOT, STATIC_ROOT
from blog.feeds import RSS_URLS
from blog.sitemaps import SITEMAPS_URLS
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pytrorg.views.home', name='home'),
    # url(r'^pytrorg/', include('pytrorg.foo.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'blog.views.blogHome', name="bloghome"),
    url(r'^admin/', include(admin.site.urls)),
    (r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT }),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT }),
)

urlpatterns += RSS_URLS
urlpatterns += SITEMAPS_URLS