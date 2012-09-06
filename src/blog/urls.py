from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
    url(r'^$', 'blogHome', name="bloghome"),
    url(r'^(?P<slug>[-\w]+)/$','blogPost', name="blogpost"),
    url(r'^kategori/(?P<slug>[-\w]+)/','blogCategory', name="blogcategory"),

)