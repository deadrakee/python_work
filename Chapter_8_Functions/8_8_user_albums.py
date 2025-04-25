### 8-8. User Albums:

def make_album(artist, title):
    """Return a dictionary"""
    current_album = {
        'artist': artist,
        'title': title,
    }
    return current_album


albums = []

while True:
    print("\nEnter album data or 'q' to quit: ")
    user_input = input("Artist: ")
    if user_input == 'q':
        break
    else:
        artist = user_input

    user_input = input("Title: ")
    if user_input == 'q':
        break
    else:
        title = user_input

    current_album = make_album(artist,title)
    albums.append(current_album)

for album in albums:
    print(album)