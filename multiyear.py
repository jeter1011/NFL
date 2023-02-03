import requests
from bs4 import BeautifulSoup
import pandas as pd

# Create a list to store the draft data
draft_data = []

# Loop through each year from 1990 to 2022
for year in range(2020, 2023):
    url = f"https://www.pro-football-reference.com/years/{year}/draft.htm"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table containing the draft data
    table = soup.find("table", {"id": "drafts"})

    if table:
        # Find all rows in the table
        rows = table.find_all("tr")

        # Loop through each row and extract the data
        for row in rows:
            cells = row.find_all("td")
            if cells:
                round_num = cells[0].text
                pick_num = cells[1].text
                team = cells[2].text
                player = cells[3].text
                position = cells[4].text
                college = cells[5].text
                draft_data.append([year, round_num, pick_num, team, player, position, college])
    else:
        print(f"Warning: Unable to find table for year {year}")

# Create a pandas DataFrame from the draft data
df = pd.DataFrame(draft_data, columns=["Year", "Round", "Pick", "Team", "Player", "Position", "College"])

# Save the DataFrame to a CSV file
df.to_csv("nfl_draft_data2.csv", index=False)
