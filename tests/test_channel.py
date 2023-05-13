from src.channel import Channel
import pytest


@pytest.fixture
def get_item():
    return Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')


def test_channel(get_item):
    assert get_item.channel_id == 'UCMCgOm8GZkHp8zJ6l7_hIuA'
    assert get_item.title == "вДудь"
    assert get_item.description == "Здесь задают вопросы"
    assert int(get_item.subs_count) >= 10300000
    assert int(get_item.video_count) >= 168
    assert int(get_item.view_count) >= 1996539103


def test_print_info(get_item):
    assert get_item.print_info() == print(str)
