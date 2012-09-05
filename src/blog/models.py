from django.db import models
from django.contrib.auth.models import User
from unidecode import unidecode
from tagging.fields import TagField, Tag

class Categories(models.Model):
    # yazi basligi ve sef turu
    title           = models.CharField(max_length=255, verbose_name="Baslik")
    sef_title       = models.CharField(max_length=255, blank=True, editable=False)

    # url slug yapisi
    slug            = models.SlugField(max_length=255, verbose_name="Slug")

    # meta descriptionda cikacak aciklama bolumu seo icin bi hayli onemli
    description     = models.CharField(max_length=255, verbose_name="Aciklama")
    sef_description = models.CharField(max_length=255, blank=True, editable=False)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Kategoriler"

    def get_absolute_url(self):
        return "/blog/kategori/%s/" %self.slug

    def save(self, *args, **kwargs):
        self.sef_title = unidecode(self.title)
        super(Categories, self).save(*args, **kwargs)

        self.sef_description = unidecode(self.description)
        super(Categories, self).save(*args, **kwargs)

class Posts(models.Model):
    # yazi basligi ve sef turu
    title           = models.CharField(max_length=255, verbose_name="Baslik")
    sef_title       = models.CharField(max_length=255, blank=True, editable=False)

    # url slug yapisi
    slug            = models.SlugField(max_length=255, verbose_name="Slug")

    # meta descriptionda cikacak aciklama bolumu seo icin bi hayli onemli
    description     = models.CharField(max_length=255, verbose_name="Aciklama")
    sef_description = models.CharField(max_length=255, blank=True, editable=False)

    # kategori secimi
    categories      = models.ManyToManyField(Categories, verbose_name="Kategoriler", blank=True)

    # yazi icerik kismi
    content         = models.TextField(verbose_name="Icerik")

    # yazi yayindami kontrolu
    isonline        = models.BooleanField(verbose_name="Yazi yayinlansin mi?", default=False)

    # etiketlerimiz
    tags            = TagField(verbose_name="Etiketler")

    # olusturulma ve degistirilme tarihleri admin panelinde gozukmez
    created         = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Olusturulma")
    edited          = models.DateTimeField(auto_now=True, editable=False, verbose_name="Degistirilme")

    # yazar secimi
    author          = models.ForeignKey(User, verbose_name="Yazar")

    # unicode fonksiyonumuz
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Yazilar"

    def get_absolute_url(self):
        return "/blog/%s/" %self.slug

    def save(self, *args, **kwargs):
        self.sef_title = unidecode(self.title)
        super(Posts, self).save(*args, **kwargs)

        self.sef_description = unidecode(self.description)
        super(Posts, self).save(*args, **kwargs)

    def get_tags(self):
        return Tag.objects.get_for_object(self)



