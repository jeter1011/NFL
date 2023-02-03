import pandas as pd
import numpy as np


df = pd.read_csv('nfl_draft_data2.csv')


df = df.rename(columns={"Year": "Draft Year",
                        "Round": "Pick",
                        "Pick": "Team",
                        "Team": "Player",
                        "Player": "Position",
                        "Position": "College",
                        "College": "Useless"})

#print(df.head(10))

# Create the Round column by dividing each pick by 32, floor dividing by 1 and then adding 1
df['Round'] = np.ceil(np.floor_divide(df['Pick'], 33) + 1)

# Print the resulting DataFrame
print(df.head(108))


# # Group the DataFrame by year and team
#grouped = df.groupby(["Draft Year", "Team"])
#
# Calculate the total number of picks for each team each year
#total_picks = grouped.size().reset_index(name="Total Picks")
#
# # Group the DataFrame by year, team, and round
# grouped = df.groupby(["Draft Year", "Team", "Pick"])

# Calculate the number of picks for each team in each round each year
# round_picks = grouped.size().reset_index(name="Round Picks")
#
# # Merge the two DataFrames on Year and Team
# result = pd.merge(total_picks, round_picks, on=["Year", "Team"])
#
# # Print the resulting DataFrame
# print(result)

