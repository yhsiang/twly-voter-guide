# -*- coding: utf-8 -*-
from django.db import models

from json_field import JSONField


class Candidates(models.Model):
    uid = models.CharField(max_length=64)
    latest_term = models.ForeignKey('legislator.LegislatorDetail', blank=True, null=True)
    legislator = models.ForeignKey('legislator.LegislatorDetail', blank=True, null=True, related_name='elected_candidate')
    ad = models.IntegerField(db_index=True, )
    number = models.IntegerField(db_index=True, blank=True, null=True)
    name = models.CharField(max_length=100)
    birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    party = models.CharField(db_index=True, max_length=100, blank=True, null=True)
    constituency = models.IntegerField(db_index=True)
    county = models.CharField(db_index=True, max_length=100)
    district = models.CharField(db_index=True, max_length=100, blank=True, null=True)
    votes = models.IntegerField(blank=True, null=True)
    votes_percentage = models.CharField(max_length=100, blank=True, null=True)
    elected = models.NullBooleanField(db_index=True)
    contact_details = JSONField(null=True)
    education = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    links = JSONField(null=True)
    platform = models.TextField(blank=True, null=True)
    politicalcontributions = JSONField(null=True)

    class Meta:
        unique_together = ('uid', 'ad')

    def __unicode__(self):
        return self.name
