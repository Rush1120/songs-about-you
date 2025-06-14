# Songs about you

A mood-based music recommender system built with the Spotify Web API, Python, and Streamlit. It analyzes your top tracks and classifies them by mood like Happy, Chill, Sad, or Hype based on their audio features.

## Features

- Login with your Spotify account
- Fetch and analyze your top tracks
- Mood classification using valence & energy
- Streamlit UI to explore tracks by mood
- Future: Playlist generation and deployment

## Tech Stack

- Python
- Spotipy (Spotify API wrapper)
- Streamlit
- Pandas
- (Optional ML with sklearn or logic rules)

## How to Run Locally

1. Clone the repo:
```bash
git clone https://github.com/Rush1120/songs-about-you.git
cd songs-about-you
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
streamlit run app.py
```

## Setup Spotify API Credentials

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create an app and get:
   - Client ID
   - Client Secret
3. Add these to a `.env` file (or directly in your script for now)

## Future Improvements

- Auto-generate playlists by mood
- Deploy online via Streamlit Cloud
- Visualize mood breakdown with graphs
- Add filters (e.g., by genre, time range)

---

Made by **Aarushi Kalia**  
Always listening. Always learning.
