import pandas as pd 

df = pd.read_csv('cricket_data.csv')

# -------------------- PANDAS --------------------

strike_rate = df['Runs'] / df['Balls_Faced'] * 100

df["strike_rate"] = df['Runs'] / df['Balls_Faced'] * 100

highest_strike_rate = strike_rate.max()

player_highest_strike_rate = strike_rate.idxmax()

top_runs_scorer = df['Runs'].max()

top_runs_index = df['Runs'].idxmax()

top_3_runs_scorer = df.sort_values(['Runs'], ascending=False)

top_3_wickets_taker = df.sort_values(['Wickets'], ascending=False)

top_3_strike_rate = df.sort_values(['strike_rate'], ascending=False)

team_total_runs = df.groupby('Team')['Runs'].sum()

highest_scoring_team = team_total_runs.max()

highest_scoring_team_index = team_total_runs.idxmax()

highest_number_6 = df['Sixes'].max()

highest_number_6_index = df['Sixes'].idxmax()

highest_number_4 = df['Fours'].max()

highest_number_4_index = df['Fours'].idxmax()

# -------------------- QUESTIONS & ANSWERS --------------------
print(f"\nQ1. What is the strike rate of all players?\nAnswer:\n{strike_rate}")
print(f"\nQ2. What is the highest strike rate?\nAnswer: {highest_strike_rate}")
print(f"\nQ3. Which player has the highest strike rate?\nAnswer:\n{df.loc[player_highest_strike_rate]}")
print(f"\nQ4. Who is the top run scorer?\nAnswer:\n{df.loc[top_runs_index]}")
print(f"\nQ5. Who are the top 3 run scorers?\nAnswer:\n{top_3_runs_scorer[:3]}")
print(f"\nQ6. Who are the top 3 wicket takers?\nAnswer:\n{top_3_wickets_taker[:3]}")
print(f"\nQ7. Who are the top 3 players by strike rate?\nAnswer:\n{top_3_strike_rate[:3]}")
print(f"\nQ8. What are the total runs scored by each team?\nAnswer:\n{team_total_runs}")
print(f"\nQ9. Which team has the highest total runs?\nAnswer: {highest_scoring_team_index}")
print(f"Total runs: {highest_scoring_team}")
print(f"\nQ10. Which player hit the most sixes?\nAnswer:\n{df.loc[highest_number_6_index]}")
print(f"\nQ11. Which player hit the most fours?\nAnswer:\n{df.loc[highest_number_4_index]}")
