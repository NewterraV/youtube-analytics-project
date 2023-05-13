from src.channel import Channel
from src.cnst import PATH_DIR_HOME
import pytest


@pytest.fixture
def get_item():
    """Фикстура экземпляра класса"""
    return Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')


@pytest.fixture
def get_path_dir_home():
    return PATH_DIR_HOME


def test_channel(get_item):
    """Тест атрибутов экземпляра класса"""
    assert get_item.channel_id == 'UCMCgOm8GZkHp8zJ6l7_hIuA'
    assert get_item.title == "вДудь"
    assert get_item.description == "Здесь задают вопросы"
    assert int(get_item.subs_count) >= 10300000
    assert int(get_item.video_count) >= 168
    assert int(get_item.view_count) >= 1996539103


def test_print_info(get_item):
    """Тест функции print_info"""
    assert get_item.print_info() == print(str)


def test_get_service(get_item):
    """Тест функции get_service()"""
    assert get_item.get_service() is not None


def test_to_json(get_item):
    assert get_item.to_json('test.json') is None
