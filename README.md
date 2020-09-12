## Web Scraper iplt20.com
___

### Description

A CLI(Command line Interface) web scraping application to extract data from https://www.iplt20.com - the official website of Indian Premier League.
The application allows user to extract following data sets from the website:
* Most Runs
* Most Runs (Over)
* Most Fours
* Most Fours (Innings)
* Most Sixes
* Most Sixes (Innings)
* Most Fifties
* Most Centuries
* Fastest Fifties
* Fastest Centuries
* Highest Scores
* Highest Scores (Innings)
* Best Batting Strike Rate
* Best Batting Average
* Biggest Sixes
* Most Wickets
* Most Maidens
* Most Dot Balls
* Most Dot Balls (Innings)
* Best Bowling Average
* Best Bowling Economy
* Best Bowling Economy (Innings)
* Best Bowling Strike Rate
* Best Bowling Strike Rate (Innings)
* Best Bowling Innings
* Most Runs Conceded (Innings)
* Fastest Balls
* Most Hat Tricks
* Most Four Wickets
* Player Points
* Team Ranking
* Team Vs Team & winner

The data is available for the years 2008-2019 along with some all season stats.
___
### Install Dependencies
```
pip install pandas
pip install numpy
pip install beautifulsoup4
pip install requests
pip install PyInquirer
```

### Run
Clone the repository, change directory to the downloaded repository and type following in terminal:
```
python ipl_data.py #for data 
python ipl_matches.py #for team vs team & winner
```
By default the application generates csv files which are saved in the same directory as of the script.
