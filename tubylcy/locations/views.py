from django.contrib.auth.models import User, Group
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import viewsets, mixins


from .models import Event, Quest
from .serializers import UserSerializer, GroupSerializer, EventSerializer, QuestSerializer


def index(request):
    return render(request, 'locations/index.html')


def about(request):
    return render(request, 'locations/about.html')


@login_required
def profile(request, username):
    if request.user.username != username:
        return redirect('/')

    ctx = {
        'events': Event.objects.filter(creator__username=username),
        'quests': Quest.objects.filter(Q(reporter__username=username) | Q(assignees__username=username))
    }

    return render(request, 'locations/profile.html', ctx)


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


class QuestViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer

    def pre_save(self, obj):
        """
        Set the object's owner, based on the incoming request.
        """
        obj.reporter = self.request.user
