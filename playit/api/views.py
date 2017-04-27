from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from playit.api.requests import CreateGameRequest
from playit.api.serializers import WordSerializer
from playit.models import  Game, Player


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
def join_game(request):
    if request.method == 'POST':
        request_obj = validate_request(join_game, request.data)
        pin_code = request_obj['pin_code']
        nickname = request_obj['nickname']
        game  = Game.objects.get(pin_code=pin_code)
        player = Player(nickname=nickname ,game=game)
        return Response(player)

@api_view(['POST'])
def start_game(request):
    if request.method == 'POST':
        request_obj = validate_request(start_game,request.data)
        pin_code = request_obj['pin_code']
        game_obj = Game.objects.get(pin_code=pin_code)
        game_obj.game_started = True
        game_obj.save()
        # todo : redirect to some sort of start game function.


@api_view(['POST'])
def get_next_question(request):
    if request.method == 'POST':
        request_obj = validate_request(get_next_question,request.data)
        pin_code = request_obj['pin_code']
        game_obj = Game.objects.get(pin_code=pin_code)
        game_manager = game_obj.game_manager
        question = game_manager.get_next_question()
        return Response(question)
        # todo : redirect to some sort of start game function.


@api_view(['GET'])
def get_players(request):
    if request.method == 'GET':
        request_obj = validate_request(get_players,request.data)
        pin_code = request_obj['pin_code']
        players = Player.objects.filter(game__pin_code=pin_code).all()
        return Response(players )




