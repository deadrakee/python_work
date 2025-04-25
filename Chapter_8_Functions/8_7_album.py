### 8-7. Album:

def make_album(artist, album, songs_number= None):
    """Creates a dictionary"""
    if songs_number:
        artist_album = {
            'artist': artist,
            'album': album,
            'songs_number': songs_number,
        }
    else:
        artist_album = {
            'artist': artist,
            'album': album,
        } 

    return artist_album

artist_album_0 = make_album('ed sheeran', 'plus')
artist_album_1 = make_album('ed sheeran', 'minus')
artist_album_2 = make_album('ed sheeran', 'autumn variations')

print(artist_album_0)
print(artist_album_1)
print(artist_album_2)

artist_album_3 = make_album('ed sheeran', 'divide', 12)
print(artist_album_3)
