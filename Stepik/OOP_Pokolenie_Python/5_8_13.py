class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getattr__(self, item):
        return len(self.__dict__) + 1

music_group = AttrsNumberObject(name='Woodkid', genre='pop')

print(music_group.attrs_num)
music_group.country = 'France'
print(music_group.attrs_num)
