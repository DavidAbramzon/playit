from rest_framework import serializers
from playit.games.emojit.models import EmojiQuestion

class EmojiQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmojiQuestion
        fields = '__all__'
