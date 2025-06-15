import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import streamlit as st

# Auth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="Your client id",
    client_secret="your secret id",
    redirect_uri="http://127.0.0.1:8000/callback",
    scope="user-top-read"
))

# Get Top Tracks
results = sp.current_user_top_tracks(limit=20, time_range='short_term')

# Mood classifier
def classify_mood(valence, energy):
    if valence > 0.6 and energy > 0.6:
        return "Happy"
    elif valence > 0.6 and energy <= 0.6:
        return "Chill"
    elif valence <= 0.6 and energy > 0.6:
        return "Hype"
    else:
        return "Sad"

# Create DataFrame
data = []
for item in results['items']:
    features = sp.audio_features(item['id'])[0]
    mood = classify_mood(features['valence'], features['energy'])
    data.append({
        "Track": item['name'],
        "Artist": item['artists'][0]['name'],
        "Valence": round(features['valence'], 2),
        "Energy": round(features['energy'], 2),
        "Mood": mood
    })

df = pd.DataFrame(data)

# --- STREAMLIT APP ---
st.title("🎧 Spotify Mood Recommender")
st.write("Based on your listening history, here's what matches your vibe.")

# Mood filter
mood = st.selectbox("Choose a Mood", ["Happy", "Chill", "Hype", "Sad"])

filtered_df = df[df['Mood'] == mood]

if not filtered_df.empty:
    st.success(f"🎶 Songs that feel {mood}:")
    st.dataframe(filtered_df[['Track', 'Artist']])
else:
    st.warning("No songs found for this mood yet. Try another!")
