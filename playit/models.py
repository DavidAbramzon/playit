import datetime

from django.db import models


class DefaultModel(models.Model):
    """
    Default Model - every model should inherit this class
    """
    created_at = models.DateTimeField(default=datetime.datetime.utcnow)
    updated_at = models.DateTimeField(default=datetime.datetime.utcnow)
    updated_by = models.IntegerField(default=-1)
    remarks = models.TextField(blank=True)

    class Meta:
        abstract = True

class GameType(DefaultModel):

    game_name = models.TextField()
    python_model_name = models.TextField()



class GameManager(DefaultModel):

    def get_next_question(self,request):
        pass

    def save_answer(self, request,player, answer):
        pass

    def get_round_summary(self,request):
        pass

    def get_score_board(self,request):
        pass

    def get_answer(self,request):
        pass

    def choose_answer(self,request):
        pass

class Game(DefaultModel):
    """
    Model for holding information about a single game
    fields - PINCODE, game type,
    """
    pin_code = models.AutoField(primary_key=True)
    game_type = models.ForeignKey(GameType)
    game_manager = models.ForeignKey(GameManager)
    game_started = models.BooleanField(default=False)

#

class Player(DefaultModel):
    game = models.ForeignKey(Game)
    nickname = models.TextField()
    score = models.IntegerField(default=0)


class Answer(DefaultModel):
    player = models.ForeignKey(Player)

