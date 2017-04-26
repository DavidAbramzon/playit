from rest_framework import serializers

from playit.models import  Work, Subtitle

from django.contrib.auth.models import User


#todo example delete me

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('word_name', 'word_score')

