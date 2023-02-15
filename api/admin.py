from django.contrib import admin
from .models import Artist, Song, Album, Track


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass


@admin.register(Song)
class Song(admin.ModelAdmin):
    pass


class TrackAdminInline(admin.TabularInline):
    model = Track
    extra = 1


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (TrackAdminInline,)
