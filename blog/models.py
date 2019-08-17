from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
CATG_CHOICES = (
    ('life','life'),
    ('thougts', 'thougts'),
    ('android','android'),
    ('web_dev','web_dev'),
    ('blog','blog'),
)

class Post (models.Model) :
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    icon = models.CharField(max_length=10, default='book')
    text = RichTextUploadingField()
    catg = models.CharField(max_length=6, choices=CATG_CHOICES, default='blog')
    desc = models.TextField(default="Description Field of the Post")
    cover = models.ImageField(upload_to = 'cover/',default='static/images/default_cover.jpg')
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

