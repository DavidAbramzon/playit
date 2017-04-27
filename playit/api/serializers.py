from rest_framework import serializers
from playit.models import GameType, Player, Game, GameManager, Answer

class GameTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameType

class GameManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameManager

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer



