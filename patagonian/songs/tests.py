from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient

from django.test.client import encode_multipart, RequestFactory

client = APIClient()
response = client.get('/songs')
assert response.status_code == 400
response = client.get('/songs?artistName=')
assert response.status_code == 400
response = client.get('/songs?artistName=ee')
assert response.status_code == 400
response = client.get('/songs?artistName=Wee')
assert response.status_code == 200
response = client.get('/songs/no_one')
assert response.status_code == 404
response = client.get('/songs/1NElFEFbyjGahnubwlSPZE')
assert response.status_code == 200
