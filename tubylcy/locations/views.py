from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from rest_framework import viewsets, mixins


from .models import Event
from .serializers import UserSerializer, GroupSerializer, EventSerializer


def index(request):
    template = loader.get_template('locations/index.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))


def about(request):
    template = loader.get_template('locations/about.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class EventViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

