from django.shortcuts import render
from rest_framework.views import Response, APIView
from rest_framework.generics import ListAPIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .models import Artist
from .serializers import ArtistSerializer


class ArtistList(ListAPIView):
    """
    Returns a list of artist objects and their albums and songs.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDetail(APIView):
    @swagger_auto_schema(responses={200: ArtistSerializer()})
    def get(self, *args, **kwargs):
        """
        Returns detailed information about the artist.
        """
        try:
            artist = Artist.objects.get(pk=kwargs.get('pk'))
        except Artist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data, status=status.HTTP_200_OK)

