from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^profile/$', 'attendance.views.profile', name='profile'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^register/$', 'attendance.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^$', 'attendance.views.dropdown', name='dropdown'),
    url(r'^admin/', include(admin.site.urls)),
)
