from django.conf import settings
from django.db import models
from django.utils import timezone

# Definición entrada del blog
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE) # key objeto
    title = models.CharField(max_length=200) # campo caracteres
    text = models.TextField() # campo de texto
    created_date = models.DateTimeField(default=timezone.now) # fecha y hora - por defecto= fecha actual
    published_date = models.DateTimeField(blank=True, null=True) # fecha y hora

    # método para publicar la entrada
    def publish(self):
        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return self.title