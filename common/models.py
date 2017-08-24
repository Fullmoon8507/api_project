from django.db import models

class account(models.Model):
    site = models.TextField(primary_key=True)
    id = models.TextField()
    pw = models.TextField()
