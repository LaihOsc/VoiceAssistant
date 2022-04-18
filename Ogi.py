import os
import time
from voice_recog import listen
import speech_recognition as sr

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from modules import search_song
from modules import process_command
import pyautogui
import secrets



id = secrets.id
secret = secrets.secret
uri = secrets.uri
scope = secrets.scope
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=id,
                                               client_secret=secret,
                                               redirect_uri=uri,
                                               scope=scope))

def Ogify():

    command = ''

    while command != 'stop':
        try:
            sentence = listen()
            if sentence == None:
                continue
            print(sentence)



            command = process_command(sentence)[0]
            query = process_command(sentence)[1]


            if command == 'music':
                if sp.currently_playing()['is_playing'] == True:
                    sp.pause_playback()
                else:
                    sp.start_playback()
            elif command == 'play':
                if sp.currently_playing()['is_playing'] == True:
                    sp.add_to_queue(search_song(query))
                    print(f'Added {query} to queue')
                    sp.next_track()
                    print('Skipped track.')
                else:
                    sp.add_to_queue(search_song(query))
                    print(f'Added {query} to queue')
                    sp.start_playback()
            elif command == 'write' or 'right':
                pyautogui.write(query)
            elif command == 'search':
                print(f'Google search for {command}')

            print('loop done')

        except sr.UnknownValueError:
            print('Didnt quite catch that')
            continue


Ogify()