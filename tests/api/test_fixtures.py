import pytest

@pytest.mark.check
def test_chanke_name(user):
    assert user.name == 'Yevhenii'

@pytest.mark.check
def test_change_second_name(user):
    assert user.second_name == 'Baburin'