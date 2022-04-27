'''This file is the main file for the application.'''
from flask import Flask, render_template
from data import get_data
import random
import os

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def hello():
    '''This function is the main function for the application.'''

    '''Artic Monkeys, Bad Bunny, Inner Wave'''
    artist_list = ['7Ln80lUS6He07XvHI8qqHH', '4q3ewBCX7sLwd24euuV69X', '6AQEfqGPSxZX0nJVonYxi6']

    rand = random.randint(0, len(artist_list) - 1)

    info = get_data(artist_list[rand])
    print(info)

    return render_template(
        'index.html',
        song_name = info[0],
        artist_names = info[1],
        album_image = info[2],
        song_preview = info[3],
        spotify_link = info[4],
        total_artists = len(info[1])
    )

if __name__ == '__main__':
    app.run(
        debug=True,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080))
    )