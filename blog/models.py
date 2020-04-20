from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    # All the models to be sent to the database must inherit from .Model
    # Define the properties our object must have #
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #Charfields are textfields with the number of characters limited in SQL. For unilimited fields use TextField#
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
