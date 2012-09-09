from django.conf.urls import patterns, url

urlpatterns = patterns('sources.views',
    url(r'^$', 'sourcesHome', name="sourceshome"),
    url(r'^(?P<slug>[-\w]+)/$','sourcesPost', name="sourcespost"),
    url(r'^kategori/(?P<slug>[-\w]+)/','sourcesCategory', name="sourcescategory"),
    url(r'^etiket/(?P<tag_name>[-\w\s]+)/','sourcesTag', name="sourcestag"),
)

