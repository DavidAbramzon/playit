from rest_framework import serializers


class SaveAnswerRequest(serializers.Serializer):
    answer = serializers.ImageField()


class GetScoreBoardRequest(serializers.Serializer):
    pin_code = serializers.IntegerField()




