import requests
from conftest import BASE_URL
# from conftest import *


host_url = "https://jsonplaceholder.typicode.com"


def test_todo():
    response = requests.get('{}/posts'.format(host_url))
    assert response.status_code == 200

    response_headers = response.headers
    # print(response_headers)
    # assert False


def test_users():
    users_list = requests.get("{}/posts/1".format(BASE_URL))
    assert users_list.status_code == 200
