from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from models import *
from django.contrib.sites.models import Site
from django.template import RequestContext
from tagging.models import Tag, TaggedItem


def sourcesHome(request):
    sources       = Sources.objects.order_by("-created").filter(isonline=True)
    source_list   = Sources.objects.order_by("-created").filter(isonline=True)[:5]
    categories    = Categories.objects.order_by("title")

    site          = Site.objects.get_current()
    return render_to_response('sources/index.html', locals(), RequestContext(request))

def sourcesPost(request, slug):
    source        = get_object_or_404(Sources, slug=slug)

    sources       = Sources.objects.order_by("-created").filter(isonline=True)[:5]
    categories    = Categories.objects.order_by("title")
    tags          = Tag.objects.all().order_by("name")[:10]

    site          = Site.objects.get_current()
    return render_to_response('sources/sources-post.html', locals(), RequestContext(request))

def sourcesCategory(request, slug):
    category      = get_object_or_404(Categories, slug=slug)

    sources       = Sources.objects.filter(categories = category).filter(isonline=True).order_by("-created")
    source_list   = Sources.objects.order_by("-created").filter(isonline=True)[:5]
    categories    = Categories.objects.order_by("title")
    tags          = Tag.objects.all().order_by("name")[:10]

    site          = Site.objects.get_current()
    return render_to_response('sources/sources-category.html', locals(), RequestContext(request))

def sourcesTag(request, tag_name):
    tag           = get_object_or_404(Tag, name=tag_name)
    sources       = TaggedItem.objects.get_by_model(Sources, tag).filter(isonline=True).order_by("-created")
    source_list   = Sources.objects.order_by("-created").filter(isonline=True)[:5]

    categories    = Categories.objects.order_by("title")
    tags          = Tag.objects.all().order_by("name")[:10]

    site          = Site.objects.get_current()
    return render_to_response('sources/sources-tag.html', locals(), RequestContext(request))
