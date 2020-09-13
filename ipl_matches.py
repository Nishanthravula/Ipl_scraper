from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

url = "https://www.iplt20.com/matches/results/men/year" #replace year with your specified year
content = requests.get(url)
f = open('data-year.csv','w', newline='')  #replace year with your specified year
writer = csv.writer(f)
soup = BeautifulSoup(content.text,'html.parser')
writer.writerow(['Home_team','Away_team','Winner'])
# print(soup.prettify())

tags = soup.findAll('p', {"class" : "result__team-name"})

a = []
for tag in tags:
    team=tag.get_text()
    a.append(team)
    # print(team)
# print(a)
wons = soup.findAll('p', {"class" : "result__outcome u-hide-phablet"})

c = []
for won in wons:
    winner = won.get_text()
    c.append(winner)
    # print(winner)

home_team = [a[i] for i in range(len(a)) if i % 2 == 0] 
away_team = [a[i] for i in range(len(a)) if i % 2 != 0]

tableData = [home_team,away_team, c]
for v in zip(*tableData):
    print(*v)
    writer.writerow(v)
