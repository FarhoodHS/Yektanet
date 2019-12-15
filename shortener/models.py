from django.db import models
from django.contrib.auth.models import User
import re

class Url(models.Model):

    original_url = models.URLField(max_length=300)
    shortened_url = models.TextField(max_length=300, unique=True, db_index=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class ClickDate(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    url = models.ForeignKey(Url, on_delete=models.PROTECT)
    is_mobile = models.BooleanField(default=False)