#-*- coding: utf-8 -*-

#django
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

urlpatterns = patterns('builder',
    
    url(r'^builder/upload$', 'views.builder_upload', name='builder_upload'),
    url(r'^builder/(?P<pid>\w+)', 'views.builder', name='builder'),
    
    
    url(r'^problems', 'views.problems', name='problems'),
    url(r'^problem/(?P<pid>\w+)', 'views.problem', name='problem'),
    url(r'^widget/(?P<pid>\w+).js$', 'views.widget_js', name='widget_js'),
    url(r'^widget/(?P<pid>\w+)$', 'views.widget', name='widget'),
    
    url(r'^api/1/problems/?$', 'views.api_1_problems', name='api_1_problems'),
    url(r'^api/1/problems/(?P<pid>\w+)/?$', 'views.api_1_problem', name='api_1_problem'),
    url(r'^api/1/problems/(?P<pid>\w+)/submissions/?$', 'views.api_1_submissions', name='api_1_submissions'),
    url(r'^api/1/problems/(?P<pid>\w+)/submissions/(?P<sid>\d+)/?$', 'views.api_1_submission', name='api_1_submission'),
    
    url(r'^', 'views.home', name='home'),
)
