from django.http import JsonResponse
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from playit.api.requests import CreateGameRequest, StartGameRequest, JoinGameRequest, GetPlayersRequest, \
    GetNextQuestionRequest, SaveAnswerRequest, getRoundSummaryRequest, GetScoreBoardRequest, GetGameByPincode
from playit.api.serializers import *
from playit.models import Game, Player, GameType, GameManager
import tempfile




def validate_request(serializer, request_data):
    request_obj = serializer(data=request_data)
    request_obj.is_valid(raise_exception=True)
    return request_obj.validated_data

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
        game_type_obj = GameType.objects.get(id=request_obj['game_type_id'])
        # todo : need to import from module name
        from django.utils.module_loading import import_string

        game_manager_module = import_string(game_type_obj.python_model_name)
        new_game_manager = game_manager_module()
        new_game_manager.save()
        return_game = Game(game_type=game_type_obj,game_manager=new_game_manager)
        return_game.save()
        serializer = GameSerializer(return_game)
        return Response(serializer.data)

@api_view(['POST'])
def join_game(request):
    if request.method == 'POST':
        request_obj = validate_request(JoinGameRequest, request.data)
        pin_code = request_obj['pin_code']
        nickname = request_obj['nickname']
        game = Game.objects.get(pin_code=pin_code)
        player = Player(nickname=nickname ,game=game)
        player.save()
        request.session['pin_code'] = pin_code
        request.session['player_id'] = player.id

        serializer = PlayerSerializer(player)
        return Response(serializer.data)

@api_view(['POST'])
def start_game(request):
    if request.method == 'POST':
        request_obj = validate_request(StartGameRequest, request.data)
        pin_code = request.session['pin_code']
        game_obj = Game.objects.get(pin_code=pin_code)
        game_obj.game_started = True
        game_obj.save()
        serializer = GameSerializer(game_obj)
        return Response(serializer.data)


@api_view(['GET'])
def get_next_question(request):
    if request.method == 'GET':
        request_obj = validate_request(GetNextQuestionRequest,request.data)
        pin_code = request.session['pin_code']
        game_obj = Game.objects.get(pin_code=pin_code)
        game_manager = game_obj.game_manager
        question = game_manager.get_next_question(request)
        return Response(question)




@api_view(['GET'])
def get_players(request):
    if request.method == 'GET':
        request_obj = validate_request(GetPlayersRequest,request.GET)
        pin_code = request.session['pin_code']
        players = Player.objects.filter(game__pin_code=pin_code).all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_session_object(request):
    if request.method == 'GET':
        return Response(request.session)


@api_view(['POST'])
def save_answer(request):
    if request.method == 'POST':
        request_obj = validate_request(SaveAnswerRequest, request.data)
        pin_code = request.session['pin_code']
        player = Player.objects.get(id = request.session['player_id'])
        ans = request_obj['answer'].replace("data:image/png;base64,","")
        fh = open("imageToSave.png", "wb")
        fh.write(ans.decode('base64'))

        fh.close()
        fh = open("imageToSave.png", "r")
        fh.write(ans.decode('base64'))
        fh.close()
        game_obj = Game.objects.get(pin_code=pin_code)
        game_manager = game_obj.game_manager
        ok = game_manager.save_answer(request, player, ans)
        return Response(ok)

@api_view(['GET'])
def get_round_summary(request):
    if request.method == 'GET':
        request_obj = validate_request(getRoundSummaryRequest,request.data)
        pin_code = request_obj['pin_code']
        game_obj = Game.objects.get(pin_code=pin_code)
        game_manager = game_obj.game_manager
        summary = game_manager.get_round_summary()
        return Response(summary)

@api_view(['GET'])
def get_score_board(request):
    if request.method == 'GET':
        request_obj = validate_request(GetScoreBoardRequest,request.data)
        pin_code = request_obj['pin_code']
        game_obj = Game.objects.get(pin_code=pin_code)
        game_manager = game_obj.game_manager
        score_board = game_manager.get_score_board()
        return Response(score_board)


@api_view(['GET'])
def get_game_by_pincode(request):
    if request.method == 'GET':
        request_obj = validate_request(GetGameByPincode,request.GET)
        pin_code = request_obj['pin_code']
        game_obj = Game.objects.get(pin_code=pin_code)
        serializer = GameSerializer(game_obj)
        return Response(serializer.data)









