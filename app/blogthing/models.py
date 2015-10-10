from django.db import models

# Create your models here.

class Blog(models.Model):
    class Meta:
        db_table = 'blog'

    key = models.CharField(primary_key=true, max_length=256)