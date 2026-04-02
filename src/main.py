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

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        reasons = [reason.strip() for reason in explanation.split(",") if reason.strip()]

        print("---")
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
