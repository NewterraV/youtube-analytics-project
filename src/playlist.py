from src.youtubeapi import YouTubeAPI
import isodate


class PlayList(YouTubeAPI):
    """Класс для работы с плейлистами, наследуется от базового класса работы с API 'YouTubeAPI'"""
    __slots__ = 'pl_id'

    def __init__(self, pl_id):

        super().__init__()
        self.__pl_id = pl_id
        pl_videos = self.get_pl_videos(self.__pl_id)

        # Получение списка ID видео плейлиста
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in pl_videos['items']]
        self.__vd_stat = self.get_statistic_video(video_ids)

        self.__total_duration = self._get_total_duration()

        self.title = self.get_title(pl_videos)
        self.url = 'https://www.youtube.com/playlist?list=' + self.__pl_id

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.__pl_id}", "{self.title}"'

    def __str__(self):
        return f'{self.title} ({self.url})'

    @property
    def total_duration(self):
        """Возвращает объект класса datetime.timedelta с суммарной длительность плейлиста"""
        return self.__total_duration

    def show_best_video(self):
        """Возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)"""
        video_id = None
        like_count = 0
        for i in self.__vd_stat['items']:
            if int(i['statistics']['likeCount']) > like_count:
                video_id = i['id']
                like_count = int(i['statistics']['likeCount'])
        return 'https://youtu.be/' + video_id

    def _get_total_duration(self):
        """Функция получает общую продолжительность видео из списка"""
        total_time = None
        for video in self.__vd_stat['items']:
            tm = isodate.parse_duration(video['contentDetails']['duration'])
            if total_time is None:
                total_time = tm
            else:
                total_time += tm
        return total_time

    def get_title(self, pl_videos):
        """Получает имя плейлиста на основе его ID"""
        channel_id = pl_videos["items"][0]["snippet"]["channelId"]
        lst_pl = self.get_playlists(channel_id)
        pl_dict = {}
        for i in lst_pl['items']:
            pl_dict[i['id']] = i['snippet']['title']

        return pl_dict[self.__pl_id]
