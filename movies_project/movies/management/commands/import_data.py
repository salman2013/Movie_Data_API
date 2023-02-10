

from django.core.management.base import BaseCommand
import json
from movies.models import Movie


class Command(BaseCommand):
    help = 'Import data from a JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument(
            'file', type=str, help='Import data from a JSON file into the database')

    def handle(self, *args, **options):
        file = options['file']
        with open(file) as f:
            data = json.load(f)
            for item in data:
                Movie.objects.get_or_create(**item)
        self.stdout.write(self.style.SUCCESS(
            f'Successfully imported data from {file}'))
