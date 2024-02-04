import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 54
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('viktoriapakhomova_repo_not_exist')
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_singl_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0


@pytest.mark.api
def test_emoji_list_not_empty(github_api):
    r = github_api.get_emoji_list()
    assert len(r) != 0


@pytest.mark.api
def test_commit_list_not_empty(github_api):
    r = github_api.get_commit_list()
    assert len(r) != 0


@pytest.mark.api
def test_commit_author_name(github_api):
    r = github_api.get_commit_list()
    assert r[0]['commit']['author']['name'] == 'Viktoria Pakhomova'

