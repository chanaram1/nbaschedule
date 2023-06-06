import requests
from bs4 import BeautifulSoup

# Send a GET request to the NBA schedule URL
url = "https://www.espn.com/nba/schedule"
response = requests.get(url)

# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, "html.parser")

divs = soup.find_all("div", class_="ScheduleTables mb5 ScheduleTables--nba ScheduleTables--basketball")
for div in divs:
    date_element = div.find("div", class_="Table__Title")
    date = date_element.get_text().strip()

    games = div.find_all("tr", class_="Table__TR Table__TR--sm Table__even")
    for game in games:
        teams = game.find_all("span", class_="Table__Team")
        homeTeam = teams[1].get_text().strip()  # Assuming the first element is the home team
        awayTeam = teams[0].get_text().strip()  # Assuming the second element is the away team

        time_element = game.find("td", class_="date__col Table__TD")
        time = time_element.get_text().strip()

        print(date)
        print(f"{awayTeam} @ {homeTeam} - {time}")
        print("---")
