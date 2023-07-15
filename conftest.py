import pytest


class User:
    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def crate(self):
        self.name = "Yevhenii"
        self.second_name = "Baburin"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.crate()

    yield user

    user.remove
