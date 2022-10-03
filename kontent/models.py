from django.db import models

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    module = models.TextField()
    students = models.IntegerField(blank=False, null=False)
    description = models.TextField()
    is_active = models.BooleanField(default=False, null=False)
