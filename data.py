from auth import get_auth
import random
import requests

def get_data():
    access_token = get_auth()
    headers = {
        'Authorization': 'Bearer {TOKEN}'.format(TOKEN=access_token)
    }
    
    URL = 'https://api.spotify.com/v1/artists/{id}/top-tracks'.format(id='4q3ewBCX7sLwd24euuV69X')
    data = requests.get(URL + "?market=US", headers = headers)
    
    data = data.json()
    
    #rand = random.randint(0, len(data['tracks']) - 1)
    rand = 2

    artist_names = []
    for i in data["tracks"][rand]["artists"]:
        artist_names.append(i["name"])


    song_name = data["tracks"][rand]["name"]

    album_image = data["tracks"][rand]["album"]["images"][0]["url"] # Could also be null

    song_preview = data["tracks"][rand]["preview_url"] # Can be Null

    spotify_link = data["tracks"][rand]["external_urls"]["spotify"]

    info = [song_name, artist_names, album_image, song_preview, spotify_link]

    return info

    
if __name__ == '__main__':
    x = get_data()
    print(x)
   