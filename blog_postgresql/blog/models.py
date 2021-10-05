from django.db import models
from django.db.models.fields import CharField, TextField
import datetime
# Create your models here.
class Post(models.Model):
    title = CharField(max_length= 10000)
    content = TextField(max_length = 1000000)
    date = models.DateTimeField(blank=True)