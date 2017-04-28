import datetime

from django.core.files import File
from django.db import models
import playit.models as FW
import api.requests


def validate_request(serializer, request_data):
    request_obj = serializer(data=request_data)
    request_obj.is_valid(raise_exception=True)
    return request_obj.validated_data




class EmojiQuestion(FW.Question):
    emoji_name = models.TextField()
    face = models.ImageField()



class EmojiGameManager(FW.GameManager):
    def get_next_question(self, request):
        from playit.games.emojit.api.serializers import EmojiQuestionSerializer

        pin_code = request.session['pin_code']
        game_obj = FW.Game.objects.get(pin_code=pin_code)
        round_number = game_obj.round_number

        next_question = EmojiQuestion.objects.get(id=round_number)
        serilzer = EmojiQuestionSerializer(next_question)
        return serilzer.data

    def save_answer(self, request, player):
        request_obj = validate_request(api.requests.SaveAnswerRequest, request.data)
        pin_code = request.session['pin_code']
        player = request.session['player']
        ans = request_obj['answer']
        game_obj = FW.Game.objects.get(pin_code=pin_code)
        player_round_score = self.analyze_answer(ans)
        player.last_round_score = player_round_score
        # update score
        player_score = player.score
        player.score = player_score + player_round_score
        player.save()

        return ("ok")

    def get_round_summary(self, request):
        pin_code = request.session['pin_code']
        game_obj = FW.Game.objects.get(pin_code=pin_code)
        round = game_obj.round_number
        game_obj.round_number = round+1
        game_obj.save()
        FW.player.objects.values_list('nickname', 'last_round_score')

    def get_score_board(self, request):
        FW.player.objects.values_list('nickname', 'score')

    def get_answer(self, request):
        pass

    def choose_answer(self, request):
        pass

    def analyze_answer(self, image):
        # max score=100
        # min score =0



        return (partA + partB + partC)


    def teeth_shape_of_eyes(ans_array):
        res=0
        value= (2*ans_array[41][1]-ans_array[37][1]-ans_array[40][1]) + (2*ans_array[47][1]-ans_array[43][1]-ans_array[46][1])
        res = 80 - value
        if (res < 0):
            res = 0
        return res

    def teeth_shape_of_mouth(ans_array):
        res=0
        value = (ans_array[55][0]-ans_array[49][0])*(ans_array[58][1]-ans_array[52][1])
        if (value<10):
            res=50
        elif (value<20):
            res = 30
        elif (value< 30):
            res = 10
        return res

    def teeth_area_of_mouth(ans_array):
        res=0
        value = (abs(ans_array[50][1]-ans_array[54][1])+abs(ans_array[60][1]-ans_array[56][1]))
        if (value>5000):
            res = 10
        if (value>5000):
            res = 15
        if (value > 8000):
            res = 20
        if (value > 10000):
            res = 25
        if (value > 13000):
            res = 35
        if (value > 16000):
            res = 50
        return res

    def right_evy_opened(ans_array):
        res = 0
        value = (abs(ans_array[47][1] - ans_array[45][1]) + abs(ans_array[48][1] - ans_array[44][1]))
        if (value>30):
            res = 30
        elif (value>15):
            res = 10
        return res
    def left_evy_opened(ans_array):
        res = 0
        value = (abs(ans_array[42][1] - ans_array[38][1]) + abs(ans_array[41][1] - ans_array[39][1]))
        if (value>30):
            res = 30
        elif (value>15):
            res = 10
        return res
    def open_eyes(ans_array):
        res = 0  # score up to 40
        left = EmojiGameManager.left_evy_opened(ans_array)
        right = EmojiGameManager.right_evy_opened(ans_array)
        res = left + right
        return res


    def big_smile(ans_array):
        res=0 #score up to 40
        #estimate with face proportion.
        # (55x-49x)/(13x-5x)>0.6
        relation = ((ans_array[55][0]-ans_array[49][0])/(ans_array[13][0]-ans_array[5][0]))
        if (relation > 0.3):
            res=10
        elif (relation>0.4):
            res=20
        elif (relation>0.5):
            res=30
        elif (relation>0.65):
            res=40
        return res

    def large_smile(ans_array):
        res =0
        relation = (ans_array[58][1] - ((ans_array[55][1]) + (ans_array[49][1]))/2)
        res = 2*relation
        return res

    def high_eyebrows(ans_array):
        res =0

        return res






