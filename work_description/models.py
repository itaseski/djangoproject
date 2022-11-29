from django.db import models

from time import timezone


class Part(models.Model):
    title = models.CharField(max_length=128)
    publish = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Category(models.Model):
    title = models.CharField(max_length=128)
    publish = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    part = models.ForeignKey(Part, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class WorkDescription(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    publish = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


