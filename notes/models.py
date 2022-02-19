from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
