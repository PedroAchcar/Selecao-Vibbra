from rest_framework import serializers

from times.models import Time


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ['id', 'project_id', 'user_id', 'started_at', 'ended_at']