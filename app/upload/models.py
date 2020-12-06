from django.db import models

# Create your models here.

class TestModel(models.Model):
    key1 = models.CharField(max_length=20)
    key2 = models.IntegerField()
    key3 = models.FloatField()
    key4 = models.TextField(max_length=2000)

    def __str__(self):
        return self.key1