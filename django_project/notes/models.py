from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

class Topic(MPTTModel, TitleSlugDescriptionModel, TimeStampedModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('notes:topic-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class Note(TimeStampedModel):
    title = models.CharField(max_length=256)
    body = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def get_absolute_url(self):
        return reverse('notes:note-detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.title
    