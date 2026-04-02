import csv

from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        """Initialize the recommender with a song catalog."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return up to k recommended songs for a user profile."""
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return a human-readable explanation for a song recommendation."""
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into a list of dictionaries."""
    numeric_fields = {
        "id",
        "energy",
        "tempo_bpm",
        "valence",
        "danceability",
        "acousticness",
        "instrumentalness",
        "speechiness",
    }

    try:
        with open(csv_path, mode="r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            songs: List[Dict] = []

            for row in reader:
                song: Dict = {}
                for key, value in row.items():
                    if key in numeric_fields and value != "":
                        if key == "id":
                            song[key] = int(float(value))
                        else:
                            song[key] = float(value)
                    else:
                        song[key] = value
                songs.append(song)

            return songs
    except FileNotFoundError:
        print(f"Error: file not found at {csv_path}")
    except OSError as error:
        print(f"Error reading {csv_path}: {error}")

    return []


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against user preferences and return score reasons."""
    total_score = 0.0
    reasons: List[str] = []

    user_genre = str(user_prefs.get("genre", "")).strip().lower()
    song_genre = str(song.get("genre", "")).strip().lower()
    if user_genre and user_genre == song_genre:
        total_score += 1.0
        reasons.append("genre match (+1.0)")

    user_mood = str(user_prefs.get("mood", "")).strip().lower()
    song_mood = str(song.get("mood", "")).strip().lower()
    if user_mood and user_mood == song_mood:
        total_score += 1.0
        reasons.append("mood match (+1.0)")

    target_energy = float(user_prefs.get("energy", 0.0))
    song_energy = float(song.get("energy", 0.0))
    energy_similarity = 1.0 - abs(target_energy - song_energy)
    energy_points = 2.0 * energy_similarity
    total_score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    return total_score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top-k songs ranked by recommendation score."""
    scored_songs: List[Tuple[Dict, float, str]] = []

    for song in songs:
        total_score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_songs.append((song, total_score, explanation))

    # Use a non-mutating sort to preserve the input song order/list for callers.
    ranked_songs = sorted(scored_songs, key=lambda item: item[1], reverse=True)

    top_k = max(0, k)
    return ranked_songs[:top_k]
