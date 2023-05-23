from src.channel import Channel


class Video:
    """Класс работающий со статисткой видео по Id"""

    def __init__(self, video_id):
        response = Channel.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                       id=video_id).execute()
        self.__video_id = video_id
        self.title = response['items'][0]['snippet']['title']
        self.url = 'https://youtu.be/' + video_id
        self.view_count = int(response['items'][0]['statistics']['viewCount'])
        self.like_count = int(response['items'][0]['statistics']['likeCount'])

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__video_id}, {self.title})'

    def __str__(self):
        return f'{self.title}'

    @property
    def video_id(self):
        """возвращает значение __video_id"""
        return self.__video_id
