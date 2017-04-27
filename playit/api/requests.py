from rest_framework import serializers

## view requests
class JoinGameRequest(serializers.Serializer):
    pin_code = serializers.IntegerField()
    nickname = serializers.CharField()


class CreateGameRequest(serializers.Serializer):
    game_type_id = serializers.IntegerField()


class StartGameRequest(serializers.Serializer):
    pin_code = serializers.IntegerField()


class GetPlayersRequest(serializers.Serializer):
    pin_code = serializers.IntegerField()





