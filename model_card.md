# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**

---

## 2. Intended Use

Describe what your recommender is designed to do and who it is for.

Prompts:

This recommender is designed to suggest songs that match a user's stated music taste, especially their preferred genre, mood, and energy level. It assumes the user can describe what kind of vibe they want in simple terms. This is for classroom exploration and learning, not for real-world music recommendations.

---

## 3. How the Model Works

Explain your scoring approach in simple language.

Prompts:

The model looks at song features like genre, mood, energy, tempo, valence, danceability, and acousticness. It compares those features to the user's preferences, such as favorite genre, favorite mood, and target energy. Songs get points when they match the user closely, and songs with closer energy values get more points than songs that are far away. I changed the starter logic so the recommender uses a weighted scoring system instead of returning songs in a fixed order.

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data

Describe the dataset the model uses.

Prompts:

The catalog has 20 songs in data/songs.csv. It includes a mix of genres and moods such as pop, lofi, rock, ambient, jazz, synthwave, indie pop, and more. I added extra songs and extra features like instrumentalness and speechiness to make the simulation richer. Some parts of music taste are still missing, such as lyrics, artist popularity, and listener history.

---

## 5. Strengths

Where does your system seem to work well

Prompts:

- User types for which it gives reasonable results
- Any patterns you think your scoring captures correctly
- Cases where the recommendations matched your intuition

This system works well for users who describe their taste in clear vibe terms like pop, lofi, or rock. It does a good job of putting high-energy pop songs near a High-Energy Pop profile, relaxing lofi songs near a Chill Lofi profile, and intense rock songs near a Deep Intense Rock profile. The scoring also captures the idea that energy matters a lot when users want songs that feel upbeat, calm, or intense.

---

## 6. Limitations and Bias

Where the system struggles or behaves unfairly.

Prompts:

- Features it does not consider
- Genres or moods that are underrepresented
- Cases where the system overfits to one preference
- Ways the scoring might unintentionally favor some users

The system can create a bias toward high-energy songs because energy has the strongest multiplier in the score. That means a song can still rank fairly high even when its mood is not a perfect match, especially if the energy value is close to the target. The model also does not consider lyrics, artist diversity, listening history, or context like time of day, so it may ignore important parts of real musical taste. Because the catalog is small, repeated artists or repeated high-energy songs can show up across multiple profiles and create a mild filter bubble.

---

## 7. Evaluation

How you checked whether the recommender behaved as expected.

Prompts:

- Which user profiles you tested
- What you looked for in the recommendations
- What surprised you
- Any simple tests or comparisons you ran

No need for numeric metrics unless you created some.

I tested four main profiles: a High-Energy Pop profile, a Chill Lofi profile, a Deep Intense Rock profile, and an adversarial profile with conflicting preferences such as high energy but a sad mood. I looked at whether the top results matched the intended vibe and whether the same songs kept appearing across different profiles. The Pop, Lofi, and Rock profiles mostly behaved as expected, but the adversarial profile showed that energy can still pull songs upward even when mood disagrees. That comparison helped me see that the weighting system is understandable, but it still needs tuning if I want mood to matter more in conflict cases.

---

## 8. Future Work

Ideas for how you would improve the model next.

Prompts:

- Additional features or preferences
- Better ways to explain recommendations
- Improving diversity among the top results
- Handling more complex user tastes

One improvement would be to add a Diversity Bonus so the same artist does not appear twice in the top results. Another improvement would be to use a logarithmic scale or a softer curve for tempo so small differences do not affect the score too harshly. I would also consider adding valence or danceability as stronger signals, because they can help the model separate happy music from moody music more accurately.

---

## 9. Personal Reflection

A few sentences about your experience.

Prompts:

- What you learned about recommender systems
- Something unexpected or interesting you discovered
- How this changed the way you think about music recommendation apps

This project showed me that recommender systems are not just about sorting songs by category. The weights I chose changed the personality of the system, and even small adjustments could make the results feel more like a vibe matcher or more like a genre matcher. I also learned that real recommendation systems need to balance accuracy, diversity, and fairness instead of only chasing the highest score.
