from django.db import models

class Note(models.Model):

    title = models.CharField(max_length=50,
                             unique=True
                            )
    
    text = models.TextField()

    def __str__(self):
        return self.title