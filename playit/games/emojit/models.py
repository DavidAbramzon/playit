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
        partA = self.firstTest(image)
        partB = self.secondTest(image)
        partC = self.thirdTest(image)
        return (partA + partB + partC)

    def firstTest(image):
        res = 0
        # test based of some sort of something.
        # score between 0-20
        return res

    def secondTest(image):
        res = 0
        # test based of some sort of something.
        # score between 0-40
        return res

    def thirdTest(image):
        res = 0
        # test based of some sort of something.
        # score between 0-40
        return res

    def big_smile(ans_array):
        res=0 #score up to 40
        #estimate with face proportion.
        # (55x-49x)/(13x-5x)>0.6
        relation = ((ans_array[55][0]-ans_array[49][0])/(ans_array[13][0]-ans_array[5][0]))
        if (relation > 0.3):
            res=10
        if (relation>0.4):
            res=20
        if (relation>0.5):
            res=30
        if (relation>0.65):
            res=40
        return res

    def open_eyes(ans_array):
        res = 0  # score up to 40
        relation = abs(-5)



