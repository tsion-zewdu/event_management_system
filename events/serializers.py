from rest_framework import serializers
from .models import Event, RSVP


class EventSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'created_by']
        read_only_fields = ['creator']

class RSVPSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = RSVP
        fields = '__all__'
        read_only_fields = ['user']