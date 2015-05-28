#-*- coding: utf-8 -*-

from django.db import models, IntegrityError
from django.contrib.auth.models import User

from sphere_engine import SphereEngineClient
from django.conf import settings

from django.utils import timezone

import json
import uuid
import code

from logging import Logger
logger = Logger(__file__)

# Create your models here.

class Language(models.Model):
    label = models.CharField(max_length=32)
    version = models.CharField(max_length=32)
    remote_id = models.IntegerField()
    visible = models.BooleanField(default=True)
    
    def __unicode__(self):
        return u'%s' % self.label
    
    @staticmethod
    def sync_languages():
        client = SphereEngineClient(settings.SPHERE_ENGINE_TOKEN)
        languages = client.problems.languages()
        languages = json.loads(languages)
        
        for language in languages:
            l = Language()
            l.label = language['name']
            l.version = language['ver']
            l.remote_id = language['id']
            l.save()
        

PROBLEM_RANK = (
    ('bin-date', 'Binary by date'),
    ('bin-time', 'Binary by time'),
    ('bin-source', 'Binary by length of source code'),
                )

class Problem(models.Model):
    
    code = models.CharField(max_length=8, unique=True)
    date = models.DateTimeField()
    remote_code = models.CharField(max_length=32)
    user = models.ForeignKey(User, blank=True, null=True)
    secret = models.CharField(max_length=40)
    saved = models.BooleanField(default=False)
    
    name = models.CharField(max_length=128)
    content = models.TextField()
    input = models.FileField(upload_to='uploaded')
    output = models.FileField(upload_to='uploaded')
    rank = models.CharField(max_length=16, choices=PROBLEM_RANK)
    languages = models.ManyToManyField('Language')
    date_start = models.DateTimeField(blank=True, null=True)
    date_stop = models.DateTimeField(blank=True, null=True)
    website = models.URLField(blank=True)
    resource = models.CharField(max_length=128, blank=True)
    email = models.EmailField(blank=True)
    
    stats_visits = models.IntegerField(default=0)
    stats_submissions = models.IntegerField(default=0)
    
    @staticmethod
    def create_problem(user=None):
        i = 0
        while True:
            code = str(uuid.uuid1())[0:8]
            secret = str(uuid.uuid1())
            try:
                problem = Problem()
                problem.code = code
                problem.secret = secret
                problem.date = timezone.now()
                problem.user = user
                problem.save()
                return problem
            
            except IntegrityError as e:
                logger.exception(e)
                i = i + 1
                if i > 10:
                    raise Exception('create_problem exception')
            
    
    def __unicode__(self):
        return u'%s. %s' % (str(self.id), self.name)

class ProblemFile(models.Model):
    name = models.CharField(max_length=128)
    oname = models.CharField(max_length=128)
    problem = models.ForeignKey('Problem')

class Submission(models.Model):
    date = models.DateTimeField()
    problem = models.ForeignKey(Problem)
    language = models.ForeignKey('Language')
    status = models.IntegerField(default=0)
    time = models.FloatField(default=0.0)
    mem = models.IntegerField(default=0)
    remote_id = models.IntegerField(default=0)
    
    def __unicode__(self):
        return u'%s' % str(self.id)

#
