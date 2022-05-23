from django.db import models

class Movie(models.Model):
    class Meta:
        db_table = 'movies'
    name = models.CharField(max_length=255)
    overview = models.TextField(null=1)
    image_url = models.TextField(null=1)
    score = models.IntegerField(null=1)
    release_date = models.DateField(null=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
