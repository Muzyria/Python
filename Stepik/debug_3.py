songs_db = [ {
 'artist': 'Led Zeppelin',
 'title': 'Stairways to heaven',
 'playback': '09:20'
}, {
 'artist': 'Metallica',
 'title': 'Master of puppets',
 'playback': '04:30'
}, {
 'artist': 'Nirvana',
 'title': 'The Man who sold the world',
 'playback': '03:10'
}, {
 'artist': 'Stepan',
 'title': 'Letter to mom',
 'playback': '02:20'
}]


def get_song(song_list, seconds):
    for item in song_list:
        time_song = int(item['playback'][:2]) * 60 + int(item['playback'][3:])
        if time_song < seconds:
            return item['artist'], item['title']


print(get_song(songs_db, 190))


