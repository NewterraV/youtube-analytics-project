import json
import os
from src.cnst import PATH_DIR_HOME
from src.youtubeapi import YouTubeAPI


class Channel(YouTubeAPI):
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        super().__init__()
        self.__channel_id = channel_id
        channel_dct = self.get_channel_data(self.__channel_id)
        self.title = channel_dct['items'][0]['snippet']['title']
        self.description = channel_dct['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/channel/' + self.__channel_id
        self.subs_count = int(channel_dct['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(channel_dct['items'][0]['statistics']['videoCount'])
        self.view_count = int(channel_dct['items'][0]['statistics']['viewCount'])

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.title}", "{self.__channel_id}", {self.subs_count})'

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return int(self.subs_count) + int(other.subs_count)

    def __sub__(self, other):
        return int(self.subs_count) - int(other.subs_count)

    def __lt__(self, other):
        return int(self.subs_count) < int(other.subs_count)

    def __le__(self, other):
        return int(self.subs_count) <= int(other.subs_count)

    def __gt__(self, other):
        return int(self.subs_count) > int(other.subs_count)

    def __ge__(self, other):
        return int(self.subs_count) >= int(other.subs_count)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.get_channel_data(self.__channel_id)
        return print(json.dumps(channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        """Возвращает __channel_id"""
        return self.__channel_id

    def to_json(self, filename):
        path_file = os.path.join(PATH_DIR_HOME, 'data', 'channels', filename)
        data = {'channel_id': self.__channel_id,
                'title': self.title,
                'description': self.description,
                'url': self.url,
                'subs_count': self.subs_count,
                'video_count': self.video_count,
                'view_count': self.view_count
                }

        with open(path_file, 'w', encoding='utf8') as f:
            json.dump(data, f, indent=1, ensure_ascii=False)
