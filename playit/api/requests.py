from rest_framework import serializers

## view requests
class CreateGameRequest(serializers.Serializer):
    game_type_id = serializers.IntegerField()


class JoinGameRequest(serializers.Serializer):
    pin_code = serializers.IntegerField()
    nickname = serializers.CharField()


class StartGameRequest(serializers.Serializer):
    pass
class GetNextQuestionRequest(serializers.Serializer):
    pass


class GetPlayersRequest(serializers.Serializer):
    pass


class SaveAnswerRequest(serializers.Serializer):
    answer = serializers.CharField()
    pass



class getRoundSummaryRequest(serializers.Serializer):
    pass


class GetScoreBoardRequest(serializers.Serializer):
    pin_code = serializers.IntegerField()


class GetGameByPincode(serializers.Serializer):
    pin_code = serializers.IntegerField()



