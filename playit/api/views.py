from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from playit.api.requests import CreateGameRequest
from playit.api.serializers import WordSerializer
from playit.models import  Game



def validate_request(serializer, request_data):
    request_obj = serializer(data=request_data)
    request_obj.is_valid(raise_exception=True)
    return request_obj

# todo : example delete me
@api_view(['GET'])
def example(request):
    if request.method == 'GET':
        return_dict = {
            "test":"testasd"
        }
        return Response(return_dict)


@api_view(['POST'])
def create_game(request):
    if request.method == 'POST':
        request_obj = validate_request(CreateGameRequest,request.data)

        return_game = Game()

        return_game.save()
        return Response(return_game)

@api_view(['POST'])
def start_game(request):
    if  request.method == 'POST':
        pass


