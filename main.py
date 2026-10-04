import os
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv() 

# Connect to MySQL
engine = create_engine(
    "mysql+mysqlconnector://root:password@localhost/cricket_analyser"
)

# Load cricket data from MySQL
query = "SELECT * FROM score;"
df = pd.read_sql(query, engine)

print("\n========== CRICKET STATISTICS ANALYZER ==========")

print("\nDataset:")
print(df)

# ==================== PANDAS ANALYSIS ====================

# Strike rate
df["strike_rate"] = df["runs"] / df["balls_faced"] * 100

# Highest strike rate
highest_strike_rate = df["strike_rate"].max()
highest_strike_rate_player = df.loc[
    df["strike_rate"].idxmax(), "player"
]

# Top run scorer
highest_runs = df["runs"].max()
highest_run_scorer = df.loc[
    df["runs"].idxmax(), "player"
]

# Top 3 run scorers
top_3_run_scorers = df.sort_values(
    "runs", ascending=False
).head(3)

# Top 3 wicket takers
top_3_wicket_takers = df.sort_values(
    "wickets", ascending=False
).head(3)

# Top 3 strike rates
top_3_strike_rates = df.sort_values(
    "strike_rate", ascending=False
).head(3)

# Team total runs
team_total_runs = df.groupby("team")["runs"].sum()

# Highest scoring team
highest_scoring_team = team_total_runs.idxmax()
highest_team_runs = team_total_runs.max()

# Most sixes
most_sixes = df["sixes"].max()
most_sixes_player = df.loc[
    df["sixes"].idxmax(), "player"
]

# Most fours
most_fours = df["fours"].max()
most_fours_player = df.loc[
    df["fours"].idxmax(), "player"
]

# ==================== PANDAS RESULTS ====================

print("\n========== PANDAS ANALYSIS ==========")

print(f"\nHighest Strike Rate:")
print(f"{highest_strike_rate_player} - {highest_strike_rate:.2f}")

print(f"\nTop Run Scorer:")
print(f"{highest_run_scorer} - {highest_runs} runs")

print("\nTop 3 Run Scorers:")
print(top_3_run_scorers[["player", "team", "runs"]])

print("\nTop 3 Wicket Takers:")
print(top_3_wicket_takers[["player", "team", "wickets"]])

print("\nTop 3 Strike Rates:")
print(top_3_strike_rates[["player", "team", "strike_rate"]])

print("\nTeam Total Runs:")
print(team_total_runs)

print(f"\nHighest Scoring Team:")
print(f"{highest_scoring_team} - {highest_team_runs} runs")

print(f"\nMost Sixes:")
print(f"{most_sixes_player} - {most_sixes} sixes")

print(f"\nMost Fours:")
print(f"{most_fours_player} - {most_fours} fours")

# ==================== NUMPY ANALYSIS ====================

average_runs = np.mean(df["runs"])
median_runs = np.median(df["runs"])
highest_runs_numpy = np.max(df["runs"])
std_runs = np.std(df["runs"])
percentile_runs = np.percentile(df["runs"], 75)

performance = np.where(
    df["runs"] >= 400,
    "High_Performer",
    "Normal_Performer"
)

# ==================== NUMPY RESULTS ====================

print("\n========== NUMPY ANALYSIS ==========")

print(f"\nAverage Runs:")
print(average_runs)

print(f"\nMedian Runs:")
print(median_runs)

print(f"\nHighest Runs:")
print(highest_runs_numpy)

print(f"\nStandard Deviation of Runs:")
print(std_runs)

print(f"\n75th Percentile of Runs:")
print(percentile_runs)

print("\nPlayer Performance Classification:")
print(performance)


engine.dispose()