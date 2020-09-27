## Web Scraper iplt20.com
___

### Description

A CLI(Command line Interface) web scraping application to extract data from https://www.iplt20.com - the official website of Indian Premier League.


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
