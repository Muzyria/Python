
class Video:

    def create(self, name):
        self.name = name

    def play(self):
        print(f"воспроизведение видео {self.name}")


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx: int):
        cls.videos[video_indx].play()


v1, v2 = Video(), Video()
v1.create('Python')
v2.create('Python ООП')
YouTube.add_video(v1)
YouTube.add_video(v2)
YouTube.play(0)
YouTube.play(1)

"""

class Video:

    def __init__(self):
        self.name = None

    def create(self, name):
        self.name = name

    def play(self):
        print(f"воспроизведение видео {self.name}")


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        Video.play(cls.videos[video_indx])
"""