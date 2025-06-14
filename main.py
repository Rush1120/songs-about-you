import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="6cf3d559d4b84b19a3ffaf398b297794",
    client_secret="54aa537b92514426995d20e44bcf3861",
    redirect_uri="http://127.0.0.1:8000/callback",
    scope="user-top-read"
))


results = sp.current_user_top_tracks(limit=10, time_range='short_term')

data = []

def classify_mood(valence, energy):
    if valence > 0.6 and energy > 0.6:
        return "Happy"
    elif valence > 0.6 and energy <= 0.6:
        return "Chill"
    elif valence <= 0.6 and energy > 0.6:
        return "Hype"
    else:
        return "Sad"

print("Your Songs & Their Moods:\n")

for item in results['items']:
    track_id = item['id']
    name = item['name']
    artist = item['artists'][0]['name']
    features = sp.audio_features(track_id)[0]
    valence = features['valence']
    energy = features['energy']
    mood = classify_mood(valence, energy)
    
    data.append({
        'Track': name,
        'Artist': artist,
        'Valence': round(valence, 2),
        'Energy': round(energy, 2),
        'Mood': mood
    })

df = pd.DataFrame(data)
print(df) 

