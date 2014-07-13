from django.contrib.auth.models import User, Group
from .models import Event, Quest
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    class Meta:
        model = Event
        fields = ('id', 'description', 'title', 'point')


class QuestSerializer(serializers.HyperlinkedModelSerializer):
    reporter = UserSerializer()

    class Meta:
        model = Quest
        fields = ('id', 'description', 'title', 'point')
