from django.db import models

# Create your models here.
###

class Entry(models.Model): 
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'{self.title} - {self.created_at}'

    class Meta:
        ordering = ('created_at',)