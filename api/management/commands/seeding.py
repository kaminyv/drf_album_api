from django.core.management import BaseCommand
from api.models import Artist, Album, Song, Track


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        self.clear_data()
        self.run_seed()
        self.stdout.write('done.')

    @staticmethod
    def clear_data():
        """
        Deletes all the table data
        """
        Artist.objects.all().delete()

    @staticmethod
    def run_seed():
        """
        Seed database based
        """
        for i in range(10):
            artist = Artist.objects.create(name=f"Artist{i}")
            albums = [Album.objects.create(year=f"200{i}",
                                           artist=artist) for i in range(3)]
            songs = [Song.objects.create(title=f"Song{i}-Artist{artist.name}",
                                         artist=artist) for i in range(30)]
            album_count = 0
            track_number = 1
            for x in range(30):
                if x == 9 or x == 19:
                    album_count += 1
                    track_number = 1

                Track.objects.create(
                    song=songs[x],
                    album=albums[album_count],
                    track_number=track_number
                )

                track_number += 1
