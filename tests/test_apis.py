import requests
import pytest


def test_posts_list():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 200

    response_json = response.json()
    for response in response_json:
        assert response.get('userId') is not None
        assert response.get('id') is not None
        assert response.get('title') is not None
        assert response.get('body') is not None


def test_post():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200

    response_json = response.json()
    assert response_json.get('userId') is not None
    assert response_json.get('id') is not None
    assert response_json.get('title') is not None
    assert response_json.get('body') is not None


def test_post_comments():
    response = requests.get(
        'https://jsonplaceholder.typicode.com/posts/1/comments')
    assert response.status_code == 200

    response_json = response.json()
    for response in response_json:
        assert response.get('postId') is not None
        assert response.get('id') is not None
        assert response.get('name') is not None
        assert response.get('email') is not None
        assert response.get('body') is not None


def test_response():
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    assert response.status_code == 200

    response_json = response.json()
    for response in response_json:
        assert response.get('userId') is not None
        assert response.get('id') is not None
        assert response.get('title') is not None
        assert response.get('completed') is not None


def test_create_post():
    response = requests.post('https://jsonplaceholder.typicode.com/posts',
        {
            'title': 'new post',
            'body': 'created a new post',
            'userId': 1,

        })
    assert response.status_code == 201


def test_update_post():
    response = requests.put('https://jsonplaceholder.typicode.com/posts/1',
        {
            'id': 1,
            'title': 'new post',
            'body': 'updated a new post',
            'userId': 1,

        })
    assert response.status_code == 200


def test_delete_post():
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200


# query practices
@pytest.mark.skip(reason="Skip")
def test_display_post_id():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 200

    response_json = response.json()
    post_id = [response['id'] for response in response_json]
    print(post_id)
    assert False


# def test_response_new():
#     response = requests.get('https://dummyapi.io/')
#     assert response.status_code == 200

#     # response_json = response.json()
#     print(response)
#     assert False
