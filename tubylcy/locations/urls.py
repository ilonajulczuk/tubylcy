from django.conf.urls import patterns, include, url
from django.contrib import admin

from locations import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^event/add/$', views.AddEvent.as_view(), name='add_event'),
    url(r'^event/(?P<id>\d+)$', views.DetailEvent.as_view(), name='detail_event'),
    url(r'^event/$', views.ListEvent.as_view(), name='list_event'),
    url(r'^quest/add/$', views.AddQuest.as_view(), name='add_quest'),
    url(r'^quest/(?P<id>\d+)$', views.DetailQuest.as_view(), name='detail_quest'),
    url(r'^about$', views.about, name='about'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^admin/', include(admin.site.urls)),

)
