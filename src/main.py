"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from .recommender import load_songs, recommend_songs
except ImportError:
    from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = [
        {
            "name": "High-Energy Pop",
            "prefs": {"genre": "pop", "mood": "happy", "energy": 0.9},
        },
        {
            "name": "Chill Lofi",
            "prefs": {"genre": "lofi", "mood": "chill", "energy": 0.35},
        },
        {
            "name": "Deep Intense Rock",
            "prefs": {"genre": "rock", "mood": "intense", "energy": 0.95},
        },
        {
            "name": "Edge Case: High Energy + Sad Mood",
            "prefs": {"genre": "pop", "mood": "sad", "energy": 0.9},
        },
        {
            "name": "Edge Case: Low Energy + Intense Mood",
            "prefs": {"genre": "ambient", "mood": "intense", "energy": 0.15},
        },
    ]

    for profile in profiles:
        print(f"\n=== {profile['name']} ===")
        recommendations = recommend_songs(profile["prefs"], songs, k=5)

        for index, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            reasons = [reason.strip() for reason in explanation.split(",") if reason.strip()]

            print(f"\n--- Recommendation {index} ---")
            print(f"Title: {song['title']}")
            print(f"Artist: {song['artist']}")
            print(f"Final Score: {score:.2f}")
            print("Reasons:")
            for reason in reasons:
                print(f"- {reason}")
            print("---")
            print()


if __name__ == "__main__":
    main()
