from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from playit.api.serializers import WordSerializer






# todo : example delete me
from playit.models import Work


class WorkViewSet(viewsets.ModelViewSet):

    queryset = Work.objects.all()
    serializer_class = WordSerializer



# todo : example delete me
@api_view(['GET'])
def example(request):
    if request.method == 'GET':
        return_dict = {
            "test":"testasd"
        }
        return Response(return_dict)
