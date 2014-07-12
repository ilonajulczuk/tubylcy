from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from rest_framework import viewsets


from .serializers import UserSerializer, GroupSerializer


def index(request):
    template = loader.get_template('locations/index.html')
    context = RequestContext(request, {
        #here shit from *models* useful for webpage
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
