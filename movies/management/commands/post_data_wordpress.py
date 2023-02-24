from django.core.management.base import BaseCommand
import json
import requests
import base64
from movies.models import Movie


class Command(BaseCommand):
    help = 'Import data from a JSON file into the database'

    def handle(self, *args, **options):
        # wordpress url
        url = ''

        # wordpress admin site username
        user = ''

        # wordpress application password
        password = ''

        creds = user + ':' + password
        cred_token = base64.b64encode(creds.encode())
        header = {'Authorization': 'Basic ' + cred_token.decode('utf-8')}
        movies = Movie.objects.all()
        for model in movies:
            # Create Post data here
            post = {
                'title': model.name,
                'content': model.type,
                'status': 'publish',
                'categories': 5,
                'date': model.year,
                'description': model.description
            }

            _ = requests.post(url + '/posts', headers=header, json=post)
        self.stdout.write(self.style.SUCCESS(
            f'Successfully exported data!'))
