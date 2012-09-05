from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from models import *
from django.contrib.sites.models import Site
from django.template import RequestContext
from tagging.fields import Tag


def blogHome(request):
    posts       = Posts.objects.order_by("-created").filter(isonline=True)
    categories  = Categories.objects.order_by("title")
    tags        = Tag.objects.all().order_by("name")

    site = Site.objects.get_current()
    return render_to_response('index.html', locals(), RequestContext(request))
