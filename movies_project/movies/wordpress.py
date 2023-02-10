import requests
import base64
from movies.models import Movie

url = 'http://site.local/wp-json/wp/v2'
user = 'adminsite'
password = 'qjII 6bIq q825 ZpKd qWdz iUeC'
creds = user + ':' + password
cred_token = base64.b64encode(creds.encode())
header = {'Authorization': 'Basic ' + cred_token.decode('utf-8')}
model = Movie.objects.get(id=1)
post = {
    'title': model.name,
    'content': 'Hello, this content is published using WordPress Python Integration',
    'status': 'publish',
    'categories': 5,
    'date': '2023-01-05T11:00:00'
}

blog = requests.post(url + '/posts', headers=header, json=post)
print(blog)
