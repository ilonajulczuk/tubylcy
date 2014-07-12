from django.conf.urls import patterns, include, url
from django.contrib import admin

from locations import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tubylcy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^admin/', include(admin.site.urls)),
)
