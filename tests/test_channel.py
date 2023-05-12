from src.channel import Channel
import pytest


@pytest.fixture
def get_item():
    return Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')


def test_channel(get_item):
    assert get_item.channel_id == 'UCMCgOm8GZkHp8zJ6l7_hIuA'


def test_print_info(get_item):
    assert get_item.print_info() == print(str)
