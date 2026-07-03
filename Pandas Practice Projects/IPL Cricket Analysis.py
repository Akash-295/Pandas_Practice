
# IPL Cricket Analysis (Intermediate → Advanced)

# Which team won most matches?
# Highest run scorer?
# Average runs per match?
# Toss winner vs match winner correlation?
# Top 10 players?

import pandas as pd

print('='*25)
print("IPL CRICKET ANALYSIS")
print('='*25)

matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

print('='*25)
print("IPL DATA CLEANING")
print('='*25)

print("\n",matches.head(5))
print("\n",deliveries.head(5))
print("\n",matches.shape)
print("\n",deliveries.shape)

print("\n",matches.columns)
print("\n",deliveries.columns)

print("\n",matches.info())
print("\n",deliveries.info())

print("\n",matches.isnull().sum())
print("\n",deliveries.isnull().sum())

print("\n",matches.duplicated().sum())
print("\n",deliveries.duplicated().sum())

#renaming the team name 
team_names = {
    "Delhi Daredevils": "Delhi Capitals",
    "Kings XI Punjab": "Punjab Kings",
    "Rising Pune Supergiants": "Lucknow Super Giants",
    "Royal Challengers Bangalore": "Royal Challengers Bengaluru"
}

# Replace team names
matches = matches.replace(team_names)

# Check
# print(matches["winner"].unique())

print('='*25)
print("TEAM WHO WINS MOST MATCHES")
print('='*25)

# Most wins
most_win = matches["winner"].value_counts()
print("Team Who Wins Most Matches: \n",most_win.head(1))

print('='*25)
print("HIGHEST RUN SCORER IN IPL")
print('='*25)
#Highest Run Scorer

most_runs = deliveries.groupby("batter")["total_runs"].sum().sort_values(ascending=False)
print("Highest Run Scorer: \n",most_runs.head(1))

print('='*25)
print("AVERAGE RUNS PER MATCH ")
print('='*25)

#Average Runs Per Match

avg_runs_per_match = deliveries.groupby("match_id")["total_runs"].sum().mean()
print("Average Runs Per Match: \n",avg_runs_per_match)

print('='*25)
print("TOSS WINNER & MATCH WINNER CORELATION")
print('='*25)
#Toss Winner Vs Match winner corelation

toss_match_corelation = (matches["toss_winner"] == matches["winner"]).mean() * 100
print("Toss winner vs Match winner corelation(Toss Winner Wins the Most Matches): \n",toss_match_corelation,"%")

