from __future__ import unicode_literals

from django.db import models


class Summary(models.Model):

    id = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField()
    game = models.CharField(max_length=32)
    min = models.IntegerField()
    plays = models.IntegerField()
    wagered = models.FloatField()
    winnings = models.FloatField()
    pending = models.FloatField()
    identifier = models.CharField(max_length=32)

    def __unicode__(self):
        return u"{} {}".format(self.id, self.date)

    class Meta:
        db_table = 'summary'
        verbose_name_plural = 'summary'


class Detail(models.Model):

    id = models.BigIntegerField(primary_key=True)
    time = models.DateTimeField()
    wagered = models.FloatField()
    result = models.FloatField()
    summary_id = models.ForeignKey('Summary')
    identifier = models.CharField(max_length=32)

    def __unicode__(self):
        return u"{}".format(self.id)

    class Meta:
        db_table = 'detail'
        verbose_name_plural = 'detail'


class Description(models.Model):

    id = models.BigIntegerField(primary_key=True)
    hand = models.CharField(max_length=32)
    summ = models.IntegerField()
    cards = models.CharField(max_length=32)
    action = models.CharField(max_length=32)
    rate = models.FloatField()
    win = models.FloatField()
    detail_id = models.ForeignKey('Detail')

    def __unicode__(self):
        return u"{}".format(self.id)

    class Meta:
        db_table = 'description'
        verbose_name_plural = 'description'
