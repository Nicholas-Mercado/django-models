from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model

class Snack(models.Model):
    
    name = models.CharField(max_length=256)
    rating = models.ImageField(default=0)
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
