# Error handling in python

import requests
import pytest


# @pytest.mark.skip(reason="Skip")
def test_try_except():
    # user_id = [1, "one"]
    user_id = ["one", 1]
    for user in user_id:
        import pdb
        pdb.set_trace()
        try:
            response = requests.post(
                'https://jsonplaceholder.typicode.com/posts',
                {
                    'title': 'new post',
                    'body': 'created a new post',
                    'userId': user_id

                })
            assert response.status_code == 201
        except TypeError:
            print("Only integers are allowed")


@pytest.mark.skip(reason="Skip")
def test_error():
    user_id = [1, "one"]
    # user_id = ["one", 1]
    for user in user_id:
        # import pdb
        # pdb.set_trace()
        try:
            response = requests.get(
                'https://jsonplaceholder.typicode.com/posts/{}'.format(
                    user_id))
            assert response.status_code == 200

            response_json = response.json()
            assert response_json.get('userId') is not None
            assert response_json.get('id') is not None
            assert response_json.get('title') is not None
            assert response_json.get('body') is not None
        except TypeError:
            print("Only integers are allowed")
    response = requests.get(
        'https://jsonplaceholder.typicode.com/posts/{}'.format(user_id))
    assert response.status_code == 200

    response_json = response.json()
    assert response_json.get('userId') is not None
    assert response_json.get('id') is not None
    assert response_json.get('title') is not None
    assert response_json.get('body') is not None
