from django.db import models

class Url(models.Model):

    original_url = models.URLField(max_length=300)
    shortened_url = models.TextField(max_length=300, unique=True, db_index=True)
    clicked = models.IntegerField(default=0)


class ClickDate(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    url = models.ForeignKey(Url, on_delete=models.PROTECT)