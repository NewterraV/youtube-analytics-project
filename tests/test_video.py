import pytest

from src.video import Video, PLVideo


@pytest.fixture
def get_expml():
    return Video('9lO06Zxhu88')


@pytest.fixture
def get_exmpl_pl():
    return PLVideo('9lO06Zxhu88', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')


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


def test_plvideo(get_exmpl_pl):
    """Тест Инициализации PLVideo"""
    assert get_exmpl_pl.video_id == '9lO06Zxhu88'
    assert get_exmpl_pl.title == "Как устроена IT-столица мира / Russian Silicon Valley (English subs)"
    assert get_exmpl_pl.url == 'https://youtu.be/9lO06Zxhu88'
    assert int(get_exmpl_pl.view_count) >= 49661421
    assert int(get_exmpl_pl.like_count) >= 978113
    assert get_exmpl_pl.playlist_id == 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD'
