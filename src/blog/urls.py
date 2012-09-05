from django.conf.urls.defaults import patterns, include, url
from views import blogHome

urlpatterns = patterns('blog.views',
    url(r'^$', 'blogHome', name="bloghome")
    #url(r'^(?P<slug>.*)/$','blogPost', name="blogpost"),
    #url(r'^kategori/(?P<slug>.*)/$','blogCategory', name="blogcategory"),
)