from rest_framework import serializers
from playit.models import GameType, Player, Game, GameManager, Answer

class GameTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameType
        fields = '__all__'

class GameManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameManager
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'



