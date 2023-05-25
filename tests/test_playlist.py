import pytest
from src.playlist import PlayList
import datetime


@pytest.fixture
def get_pl():
    return PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')


def test_pl(get_pl):
    """Тест инициализации"""
    assert get_pl.title == 'Редакция. АнтиТревел'
    assert get_pl.url == 'https://www.youtube.com/playlist?list=PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb'


def test_total_duration(get_pl):
    """Тест получения общего времени плейлиста"""
    assert str(get_pl.total_duration) == "3:41:01"
    assert isinstance(get_pl.total_duration, datetime.timedelta)
    assert get_pl.total_duration.total_seconds() == 13261.0


def test_show_best_video(get_pl):
    """Тест получения ссылки на самое популярное видео плейлиста"""
    assert get_pl.show_best_video() == "https://youtu.be/9Bv2zltQKQA"
