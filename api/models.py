"""
Model view module for the api application.
"""
from django.db import models


class Artist(models.Model):
    """
    The model represents the artist.
    """
    name = models.CharField(max_length=100, help_text='Enter a name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'artist'
        verbose_name_plural = 'artists'
        ordering = ('name',)


class Song(models.Model):
    """
    The model represents the song for artist.
    """
    title = models.CharField(max_length=100, help_text='Enter a title')
    artist = models.ForeignKey('Artist',
                               related_name='songs', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'song'
        verbose_name_plural = 'songs'
        ordering = ('title',)


class Album(models.Model):
    """
    The model represents the album for artist.
    """
    year = models.SmallIntegerField(max_length=4,
                                    help_text='Enter a year create')
    artist = models.ForeignKey('Artist',
                               related_name='albums', on_delete=models.CASCADE)
    song = models.ManyToManyField('Song',
                                  related_name='tracks', through='Track')

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = 'album'
        verbose_name_plural = 'albums'
        ordering = ('year',)


class Track(models.Model):
    """
    The model represents the connection of many to many
    for the album and the songs.
    """
    track_number = models.SmallIntegerField(help_text='Enter a number track')
    album = models.ForeignKey('Album',
                              related_name='tracks', on_delete=models.CASCADE)
    song = models.ForeignKey('Song',
                             related_name='tracks', on_delete=models.CASCADE)
