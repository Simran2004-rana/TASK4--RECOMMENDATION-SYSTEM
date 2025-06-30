# Task 4: Recommendation System - CodTech Internship

# Step 1: Import Libraries
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Step 2: Create a Sample Ratings Dataset
data = {
    'User': ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E'],
    'Item': ['Item1', 'Item2', 'Item3', 'Item2', 'Item4', 'Item2', 'Item3', 'Item1', 'Item4', 'Item3'],
    'Rating': [5, 3, 4, 2, 4, 5, 3, 4, 5, 4]
}

df = pd.DataFrame(data)

# Step 3: Convert to Pivot Table
df_pivot = df.pivot(index='User', columns='Item', values='Rating').fillna(0)
print("User-Item Matrix:\n", df_pivot)

# Step 4: Compute Cosine Similarity
similarity_matrix = cosine_similarity(df_pivot)
similar_users = pd.DataFrame(similarity_matrix, index=df_pivot.index, columns=df_pivot.index)
print("\nUser Similarity Matrix:\n", similar_users)

# Step 5: Recommend Items for a Specific User (e.g., User A)
user = 'A'
user_ratings = df_pivot.loc[user]
unrated_items = user_ratings[user_ratings == 0].index

scores = {}
for item in unrated_items:
    total_sim = 0
    weighted_sum = 0
    for other_user in df_pivot.index:
        if other_user != user and df_pivot.loc[other_user, item] > 0:
            sim = similar_users.loc[user, other_user]
            weighted_sum += sim * df_pivot.loc[other_user, item]
            total_sim += sim
    scores[item] = weighted_sum / total_sim if total_sim > 0 else 0

# Step 6: Print Recommendations
recommendations = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print(f"\nTop Recommendations for User {user}:\n", recommendations)
