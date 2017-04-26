import datetime

from django.contrib.auth.models import User
from django.db import models


def user_generated_subtitle_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'generated_subtitles/user_{0}/{1}'.format(instance.user.id, filename)


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

# todo : example delete me

class Work(DefaultModel):
    """
    Model for saving movies and episodes .
     maybe the word Work is not very clear
    """
    work_name = models.CharField(max_length=50)
    work_type = models.TextField(blank=True)  ## for now text 'movie\episode' maybe in future foreign key

    # subtitle_path = models.FileField()

    def __repr__(self):
        return self.work_name

    def __unicode__(self):
        return self.work_name

# todo : example delete me

class Subtitle(DefaultModel):
    """
    Model for saving subtitle uploaded by the user
    """
    subtitle_name = models.CharField(max_length=500)
    work = models.ForeignKey(Work)  ## link to  the eposide/movie
    owner = models.ForeignKey(User)
    subtitle_path = models.FileField(upload_to="subtitles/%Y/%m/%d/")

