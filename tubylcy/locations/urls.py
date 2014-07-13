from django.conf.urls import patterns, include, url
from django.contrib import admin

from locations import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^event/add/$', views.AddEvent.as_view(), name='add_event'),
    url(r'^about$', views.about, name='about'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^admin/', include(admin.site.urls)),

)
