from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()

# Create your models here.

class POI(models.Model):
    name = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)
    geometry = models.PointField()
    # latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    # longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='poi_post')

    def __str__(self):
        return self.name