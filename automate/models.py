from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.FileField(blank=True,null=True)

    def __str__(self):
        return self.image