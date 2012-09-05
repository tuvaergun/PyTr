from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from settings import DEBUG , MEDIA_ROOT

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pytrorg.views.home', name='home'),
    # url(r'^pytrorg/', include('pytrorg.foo.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'blog.views.blogHome', name="bloghome"),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^blog/', include('blog.urls'))
)

if DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT }),
    )