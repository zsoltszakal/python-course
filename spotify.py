import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

S_CLIENT_ID = 
S_CLIENT_SECRET = 

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=S_CLIENT_ID,
                                               client_secret=S_CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"))

user_id = sp.current_user()["id"]
print(user_id)

date = input("Type the date format: YYYY-MM-DD\n")
year = date.split("-")[0]

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
data = response.text

soup = BeautifulSoup(data, "html.parser")

titles = soup.find_all(name="span", class_="chart-element__information__song")

song_titles = [songs.getText() for songs in titles]

spotify_song = []

for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        spotify_song.append(uri)
    except IndexError:
        print("Song does not exist")

pprint.pprint(spotify_song)

playlist = sp.user_playlist_create(user=user_id, name=f"{date} 100 Songs", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=spotify_song)
