from django.db import models


class Feature(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField('Date Created')
    author = models.CharField(max_length=50)
    rank = models.IntegerField(default=0)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Tech_Story(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField('Date Created')
    author = models.CharField(max_length=50)
    rank = models.IntegerField(default=0)
    features = models.ManyToManyField(Feature)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
