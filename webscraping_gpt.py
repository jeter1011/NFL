import requests
from bs4 import BeautifulSoup
import time

url = "https://www.pro-football-reference.com/years/2022/draft.htm"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
print(soup)



# # Find the table containing the draft data
table = soup.find("table", {"id": "drafts"})
print(table)
#
# if table is not None:
#     content = table.find_all('p')
#     print(content)
# else:
#     print("Didn't find what I was looking for...")


# Find all rows in the table
#rows = table.find_all("tr")

# Create a list to store the draft data
# draft_data = []
#
# # Loop through each row and extract the data
# for row in rows:
#     cells = row.find_all("td")
#     if cells:
#         round_num = cells[0].text
#         pick_num = cells[1].text
#         team = cells[2].text
#         player = cells[3].text
#         position = cells[4].text
#         college = cells[5].text
#         draft_data.append([round_num, pick_num, team, player, position, college])
#
# # Print the draft data
# for data in draft_data:
#     print(data)
