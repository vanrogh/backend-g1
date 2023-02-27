from django.db import models


class Blog(models.Model):
    objects = None
    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    owner = models.CharField(max_length=255, null=False)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'