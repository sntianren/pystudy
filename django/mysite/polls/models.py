from django.db import models
import datetime

# Create your models here.

class Poll(models.Model):
    '''Poll Class'''
    question = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()

class Choice(models.Model):
    '''Choice Class'''
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length = 200)
    votes = models.IntegerField()

    def __unicode__(self):
        return self.choice
