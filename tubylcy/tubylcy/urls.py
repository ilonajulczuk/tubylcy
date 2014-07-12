from django.contrib import admin
from django.conf.urls import patterns, url, include
from rest_framework import routers
from locations import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'events', views.EventViewSet)


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^', include('locations.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
