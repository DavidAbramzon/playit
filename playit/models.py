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


class Game(DefaultModel):
    """
    Model for holding information about a single game
    fields - PINCODE, game type,
    """
    pin_code = models.IntegerField()
    game_type = models.ForeignKey(GameType)
    game_manager = models. ForeignKey(GameManager)
    game_started = models.BooleanField()

#
class GameType(DefaultModel):

    game_name = models.TextField()
    python_model_name = models.TextField()

class Player(DefaultModel):
    game = models.ForeignKey(Game)
    nick_name = models.TextField()
    score = models.IntegerField(default=0)


class Answer(DefaultModel):
    player = models.ForeignKey(Player)


class GameManager(DefaultModel):

    def get_next_question(self):
        pass

    def save_answer(self, player):
        pass

    def get_round_summary(self):
        pass

    def get_score_board(self):
        pass

    def get_answer(self):
        pass

    def choose_answer(self):
        pass