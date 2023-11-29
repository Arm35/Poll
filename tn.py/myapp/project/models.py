from django.db import models


class Poll(models.Model):
    question = models.TextField()
    active = models.BooleanField(default=False)


class Option(models.Model):
    option = models.CharField(max_length=100)
    qoute_count = models.IntegerField(default=0)
    question = models.ForeignKey(Poll, on_delete=models.CASCADE,related_name='options')
