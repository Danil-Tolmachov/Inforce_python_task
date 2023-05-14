from freezegun import freeze_time

from core_app.utils import is_voting_ended


@freeze_time('2023-05-14T10:25:43.511Z')
def test_continuing_voting():
    assert is_voting_ended() == False


@freeze_time('2023-05-14T12:25:43.511Z')
def test_ended_voting():
    assert is_voting_ended() == True
