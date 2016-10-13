#-*- coding: utf-8 -*-

#django
from django.conf.urls import include, url
from django.views.generic import RedirectView

import django
import views
from django.contrib.auth import views as auth_views

urlpatterns = [
               
    url(r'^signup$', views.signup, name='scarky_signup'),
    url(r'^confirm/(?P<login>\w+)/(?P<code>\w+)$', views.signup_confirm, name='scarky_confirm'),
    url(r'^login$', auth_views.login, {'template_name': 'account/login.html'}, name='scarky_login'),
    url(r'^logout$', auth_views.logout, {'next_page': '/'}, name='scarky_logout'),
    #url(r'^password_change_done$', 'spox.account.views.password_change_done', name='account_password_change_done'),
    #url(r'^password_reset$', 'django.contrib.auth.views.password_reset', {'template_name': 'account/reset_password.html', 'from_email': 'no-reply@sphere-engine.com', 'is_admin_site': True}, name='account_password_reset'),
    #url(r'^password_reset_done$', 'django.contrib.auth.views.password_reset_done', {'template_name': 'account/reset_password_email_sent.html'}, name='account_password_done'),
    #url(r'^password_reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)$', 'django.contrib.auth.views.password_reset_confirm', {'template_name': 'account/reset_password_set_new.html'}, name='account_password_reset_confirm'),
    #url(r'^password_reset_complete$', 'django.contrib.auth.views.password_reset_complete', {'template_name': 'account/reset_password_done.html'}, name='account_password_complete'),
]   
    