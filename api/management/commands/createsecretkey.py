from django.core.management import BaseCommand
from django.core.management.utils import get_random_secret_key


class Command(BaseCommand):
    help = 'Generates a secret key for the project.'

    def handle(self, *args, **options):
        print('SECRET KEY:', get_random_secret_key(), sep='\n')
