from rest_framework import serializers

class TaskSerializer(serializers.Serializer):
    title = serializers.CharField()
    due_date = serializers.CharField(required=False)
    estimated_hours = serializers.FloatField()
    importance = serializers.IntegerField()
    dependencies = serializers.ListField(child=serializers.CharField(), required=False)
    score = serializers.IntegerField(read_only=True)
    explanation = serializers.CharField(read_only=True)
