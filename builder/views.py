#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.urlresolvers import reverse
import uuid
import json


from models import Problem, Language
# Create your views here.

def home(request):
    return HttpResponseRedirect(reverse('builder', args=['new',]))

def builder(request, pid):
    
    params = {}
    secret = ''
    problem = None
    
    if pid == 'new':
        params['new'] = True
        
        if request.POST:
            user = None
            if request.user.is_authenticated():
                user = request.user
            problem = Problem.create_problem(user)
            problem.name = request.POST.get('name', '')
            problem.content = request.POST.get('content', '')
            problem.save()
            
            if request.is_ajax():
                return HttpResponse(json.dumps({'pid': problem.code, 'secret': problem.secret}), content_type='application/json')
            else:
                return HttpResponseRedirect('%s?secret=%s' % (reverse('problem', args=[problem.code]), problem.secret))
        
    else:
        
        secret = request.GET.get('secret', '')
        try:
            problem = Problem.objects.get(code=pid)
            
            if (not request.user.is_authenticated() and secret != problem.secret) or \
                (request.user.is_authenticated() and problem.user != request.user):
                raise Exception('access-denied')
            
        except Problem.DoesNotExist as e:
            return HttpResponseRedirect('/?not-found')
            
        except Exception as e:
            return HttpResponseRedirect('/?access-denied')
        
        
        if request.POST:
            name = request.POST.get('name', '')
            content = request.POST.get('content', '')
            input = request.POST.get('input', '')
            output = request.POST.get('output', '')

            problem.name = name
            problem.content = content
            problem.input = input
            problem.output = output
            problem.save()

            return HttpResponseRedirect('/')
    
    languages = Language.objects.all().filter(visible=True)
    if len(languages) == 0:
        Language.sync_languages()
        languages = Language.objects.all().filter(visible=True)
    params['languages'] = languages
    
    params['problem'] = problem
    params['problem_code'] = pid
    params['problem_secret'] = secret
    return render(request, 'builder/home.html', params)

def builder_upload(request):
    file = 'sdf'
    return HttpResponse(json.dumps({'file': file}), content_type='application/json')

def problem(request, pid):
    params = {}
    
    try:
        problem = Problem.objects.get(code=pid)
    except Problem.DoesNotExist:
        return HttpResponseRedirect(reverse('problems'))
    
    #if problem.secret != request.GET.get('secret', '~!@#$%^#@#$@#!@!...'):
    #    pass
    
    # jesli jest secret to edycja i statystyki
    
    
    params['problem'] = problem
    params['host'] = request.META['HTTP_HOST']
    return render(request, 'builder/problem.html', params)

def widget_js(request, pid):
    params = {pid: pid}
    
    try:
        problem = Problem.objects.get(code=pid)
    except Problem.DoesNotExist:
        pass
    
    params['host'] = request.META['HTTP_HOST']
    params['problem'] = problem
    return render(request, 'builder/widget_js.html', params)

def widget(request, pid):
    
    params = {}
    
    try:
        problem = Problem.objects.get(code=pid)
    except Problem.DoesNotExist:
        pass
    
    return render(request, 'builder/widget.html', params)

def problems(request):
    params = {}
    return render(request, 'builder/problems.html', params)
