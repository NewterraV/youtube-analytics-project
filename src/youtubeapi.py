import os
from googleapiclient.discovery import build


class YouTubeAPI:
    """Базовый класc предоставляющий методы работы с API YouTube"""
    def __init__(self):
        self._service = build('youtube', 'v3', developerKey=os.getenv('YT_API'))

    @staticmethod
    def get_service():
        """Возвращает объект для работы с YouTube API"""
        return build('youtube', 'v3', developerKey=os.getenv('YT_API'))

    def get_channel_data(self, ch_id):
        result = self._service.channels().list(id=ch_id, part='snippet,statistics').execute()

        return result

    def get_pl_videos(self, pl_id):
        """Получает по API данные о видео в плейлисте на основе id плейлиста"""
        result = self._service.playlistItems().list(playlistId=pl_id,
                                                    part='contentDetails, snippet',
                                                    maxResults=50,
                                                    ).execute()
        return result

    def get_playlists(self, channel_id):
        """Получает по API данные о плейлистах канала на основе его id"""
        result = self._service.playlists().list(channelId=channel_id,
                                                part='snippet',
                                                maxResults=50,
                                                ).execute()
        return result

    def get_statistic_video(self, lst_id):
        """Получает по API статистику по видео на основе списка ID video"""
        result = self._service.videos().list(part='contentDetails,statistics',
                                             id=','.join(lst_id)
                                             ).execute()
        return result

    def get_video_data(self, video_id):
        result = self._service.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                  id=video_id).execute()

        return result
