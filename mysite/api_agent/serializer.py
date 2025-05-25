from rest_framework import serializers

class PromptSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    prompt = serializers.CharField()