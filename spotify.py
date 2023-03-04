import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
import speech_recognition

username = 'give your user name'
clientid = 'give your cliend ID'
clientsecret = 'give your client Secret'
uri = 'http://google.com/callback/'


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = clientid ,
                                               client_secret=clientsecret,
                                               redirect_uri=uri
                                              ))

# To print the response in readable format.
print(json.dumps(username, sort_keys=True, indent=4))


while True:
    print("Welcome to the project, " + username)
    print("0 - Exit the console")
    print("1 - Search for a Song")
    user_input = int(input("Enter Your Choice: "))
    if user_input == 1:
        search_song = input("Enter the song name: ")
        results = sp.search(search_song, 1, 0, "track")
        songs_dict = results['tracks']
        song_items = songs_dict['items']
        song = song_items[0]['external_urls']['spotify']
        webbrowser.open(song)
        print('Song has opened in your browser.')
    elif user_input == 0:
        print("Good Bye, Have a great day!")
        break
    else:
        print("Please enter valid user-input.")