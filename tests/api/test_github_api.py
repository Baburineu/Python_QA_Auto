import pytest
from modules.api.clients.github import GitHub

@pytest.mark.api
def test_git_user(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exist(github_api):
    user = github_api.get_user('butenkosergii')
    print(user)
    assert user['message'] == 'Not Found'

@pytest.mark.api
def test_search_repo(github_api):
    search = github_api.search_repo('become-qa-auto')
    print(search['total_count'])
    assert search['total_count'] == 42 
    assert 'become-qa-auto' in search['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    search = github_api.search_repo('sergiibutenqo_not_found')
    assert search['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0