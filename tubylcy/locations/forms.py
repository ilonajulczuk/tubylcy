from datetimewidget.widgets import DateTimeWidget
from django import forms
from locations.models import Event, Quest


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
            'start', 'end', 'address', 'title', 'description', 'point'
        )
        widgets = {
            'start': DateTimeWidget(usel10n=True),
            'end': DateTimeWidget(usel10n=True)
        }


class QuestForm(forms.ModelForm):
    class Meta:
        model = Quest
        fields = (
            'bounty', 'title', 'description', 'assignees', 'point'
        )
