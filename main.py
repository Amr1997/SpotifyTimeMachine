
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
#scrape the billboard top 100 by date
def get_songs_list(date):
    
    URL = 'https://www.billboard.com/charts/hot-100/'+date
    page = requests.get(URL).text
    soup = BeautifulSoup(page, 'html.parser')
    charts_title_elements = soup.findAll('h3',class_="a-no-trucate")
    artist_elements = soup.findAll('span',class_='a-no-trucate')
    charts_title = [song.getText().strip() for song in charts_title_elements]
    artist_list = [artist.getText().strip() for artist in artist_elements]
    return(charts_title,artist_list)

song_titles = get_songs_list(date)[0]
artist_name = get_songs_list(date)[1]


print(song_titles)
print(artist_name)

#spotify auth constractor
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/callback",
        client_id="55b2338b1d76464b8077d5146f724a12",
        client_secret="d15ec288fe894591a827955ca30dc9f6",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
