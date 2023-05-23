import pytest

from src.video import Video


@pytest.fixture
def get_expml():
    return Video('9lO06Zxhu88')


def test_video(get_expml):
    """Тест инициализации класса Video"""
    assert get_expml.video_id == '9lO06Zxhu88'
    assert get_expml.title == "Как устроена IT-столица мира / Russian Silicon Valley (English subs)"
    assert get_expml.url == 'https://youtu.be/9lO06Zxhu88'
    assert int(get_expml.view_count) >= 49661421
    assert int(get_expml.like_count) >= 978113


def test_repr(get_expml):
    """Тест repr"""
    assert repr(get_expml) == 'Video(9lO06Zxhu88, Как устроена IT-столица мира / Russian Silicon Valley (English subs))'


def test_str(get_expml):
    """ Тест str класса Video"""
    assert str(get_expml) == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'
