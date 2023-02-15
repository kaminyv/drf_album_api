from django.shortcuts import render
from rest_framework.views import Response, APIView
from .models import Artist
from .serializers import ArtistSerializer


class ArtistAPIView(APIView):
    def get(self, *args, **kwargs):
        queryset = Artist.objects.all()
        serializer = ArtistSerializer(queryset, many=True)
        return Response(serializer.data)
