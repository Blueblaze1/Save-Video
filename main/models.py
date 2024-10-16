from django.db import models

class Video_save(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
