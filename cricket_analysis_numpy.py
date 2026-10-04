import numpy as np 
import pandas as pd 
df = pd.read_csv('cricket_data.csv')

# -----------------------------------NUMPY------------------------------------------------------------------------

average_runs = np.mean(df['Runs'])

median_runs_scored = np.median(df['Runs'])

highest_runs = np.max(df['Runs'])

std_runs = np.std(df['Runs'])

percentile_runs = np.percentile(df['Runs'],75)

perfomance = np.where(df['Runs']>=400,
                    "High_Performer",    
                    "Normal_Performer")
# ------------------------Questions&Answers------------------------------------------------------------------------
print(f"\nQ1. What is the average number of runs scored by all players?\nAnswer: {average_runs}")

print(f"\nQ2. What is the median number of runs scored by all players?\nAnswer: {median_runs_scored}")

print(f"\nQ3. What is the highest number of runs scored by a player?\nAnswer: {highest_runs}")

print(f"\nQ4. What is the standard deviation of runs?\nAnswer: {std_runs}")

print(f"\nQ5. What is the 75th percentile of runs?\nAnswer: {percentile_runs}")

print(f"\nQ6. How are players classified based on runs?\nAnswer:\n{perfomance}")