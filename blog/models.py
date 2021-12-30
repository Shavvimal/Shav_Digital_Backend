from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify


class Categories(models.TextChoices):
    BUSINESS = 'Business'
    STOCKS = 'Stocks'
    COMMUNICATION = 'Communication'
    REAL_ESTATE = 'Real Estate'
    CODE = 'Code'
    MISC = 'Misc'


class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(
        max_length=50, choices=Categories.choices, default=Categories.MISC)
    chapter = models.IntegerField(default=0)
    chapter_title = models.CharField(max_length=200)
    sub_chapter = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    excerpt = models.CharField(max_length=150)
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=2)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = BlogPost.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = BlogPost.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        if self.featured:
            try:
                temp = BlogPost.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except BlogPost.DoesNotExist:
                pass

        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
