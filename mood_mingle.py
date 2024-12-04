import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Spotify API Credentials (replace with your own)
SPOTIPY_CLIENT_ID = 'your-spotify-client-id'
SPOTIPY_CLIENT_SECRET = 'your-spotify-client-secret'

# Mood-Based Playlist Mapping (extend or modify as desired)
MOOD_PLAYLIST_MAP = {
    'happy': ['happy', 'upbeat', 'energizing'],
    'sad': ['sad', 'melancholic', 'mellow'],
    'relaxed': ['chill', 'relaxing', 'calm'],
    'focused': ['focus', 'concentrate', 'productivity']
}

def get_user_mood():
    """Prompt user for their current mood"""
    print("How are you feeling today?")
    print("1. Happy")
    print("2. Sad")
    print("3. Relaxed")
    print("4. Focused")
    choice = input("Enter the number corresponding to your mood: ")
    return ['happy', 'sad', 'relaxed', 'focused'][int(choice) - 1]

def generate_playlist(mood):
    """Generate a playlist based on the user's mood"""
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))
    results = sp.search(q=', '.join(MOOD_PLAYLIST_MAP[mood]), type='playlist')
    playlist_uri = results['playlists']['items'][0]['uri']
    return sp.playlist_tracks(playlist_uri)

def main():
    user_mood = get_user_mood()
    playlist = generate_playlist(user_mood)
    print(f"**Your {user_mood.capitalize()} Playlist:**")
    for track in playlist['items']:
        print(f"- {track['track']['name']} by {track['track']['artists'][0]['name']}")

if __name__ == '__main__':
    main()
