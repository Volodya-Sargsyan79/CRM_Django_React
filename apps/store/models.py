from django.contrib import admin
from django.db import models
from django.utils.html import format_html

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.title}'