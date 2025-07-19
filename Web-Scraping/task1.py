##########################################################
############ Web Scraping Task 1 (YallaKora) #############
##########################################################

import requests
from bs4 import BeautifulSoup
import csv

date = input("Enter the date MM/DD/YY: ")
url_page = requests.get(f"https://www.yallakora.com/match-center?date={date}")

def main(page):
    src = BeautifulSoup(page.content, "lxml")
    tournments_details = []

    tournments = src.find_all("div", {'class': 'matchCard'})
    # print(tournments)

    def get_tournment_info(tournments):
        tournment_title = tournments.contents[1].find("h2").text.strip()
        matches_content = tournments.contents[3].find_all("div", {'class', "liItem"})
        numOfMatches = len(matches_content)

        for i in range(numOfMatches):
            # get teams names
            team_A = matches_content[i].find('div', {'class', 'teamA'}).text.strip()
            team_B = matches_content[i].find('div', {'class', 'teamB'}).text.strip()

            # get match result
            match_result = matches_content[i].find('div', {'class': 'MResult'})
            match_score = match_result.find_all('span', {'class': 'score'})
            score = f"{match_score[0].text.strip()} | {match_score[1].text.strip()}"

            # get match time
            match_time = match_result.find('span', {'class': 'time'}).text.strip()

            # print(team_A)
            # print(team_B)
            # print(score)
            # print(match_time)

            tournments_details.append({
                "Tournment": tournment_title,
                "Team A": team_A,
                "Team B": team_B,
                "Match Time": match_time,
                "Match Score": score,
            })


    for i in range(len(tournments)):
        get_tournment_info(tournments[i])

    # Implementing CSV File
    keys = tournments_details[0].keys()

    with open("D:/ITI Backend using Python/ITI_Labs/Web-Scraping/tournments-details.csv", 'w', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(tournments_details)
        print("file created")

main(url_page)