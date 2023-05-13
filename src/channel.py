import json
from googleapiclient.discovery import build
import os


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('YT_API')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        channel_dkt = self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = channel_dkt['items'][0]['snippet']['title']
        self.description = channel_dkt['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/channel/' + self.channel_id
        self.subs_count = channel_dkt['items'][0]['statistics']['subscriberCount']
        self.video_count = channel_dkt['items'][0]['statistics']['videoCount']
        self.view_count = channel_dkt['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return print(json.dumps(channel, indent=2, ensure_ascii=False))

    @staticmethod
    def get_service():
        """Возвращает объект для работы с YouTube API"""
        return build('youtube', 'v3', developerKey=os.getenv('YT_API'))
