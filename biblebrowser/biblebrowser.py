#! /usr/bin/python

# Import required libraries
import json
import datetime
from pathlib import Path
import requests
from bs4 import BeautifulSoup

# Prompts the user for passages
def userInput():
    global passageVar
    passageVar = "\n".join([str(item) for item in input("Enter the passage (separate multiple passages with a comma) or enter 'today' for the daily reading: ").split(",")])
    
    if passageVar.lower() == 'today':
        readingPlan()
    else:
        oBBScrape()

# Uses the current date to determine the reading based on the imported reading plan
def readingPlan():
    global passageVar
    path = Path(__file__).parent / "./reading-plan.json"
    with open(path, 'r') as f:
            readingPlanLst = json.load(f)

    dayOfYear = datetime.datetime.today().timetuple().tm_yday  # returns day of the year (e.g. 1 for January 1st)
    passageVar = readingPlanLst[dayOfYear-1]

    oBBScrape()

# This function scrapes the oremus Bible Browser website for the given passages
def oBBScrape():
    url = 'https://bible.oremus.org/'
    parameters = {'version':'NRSV','passages': passageVar}
    page = requests.post(url, data = parameters)
    soup = BeautifulSoup(page.text, 'html.parser')

# Uses BS to locate both the passage header and the body text
    scrip_header = soup.find_all('h2', class_='passageref')
    scrip_body = soup.find_all('div', class_='bibletext')

# Loop for finding and printing all passage instances
    for passage, text in zip(scrip_header, scrip_body):
        verseText = text.find('p')
        verseList = verseText.get_text(strip=True, separator='\n').splitlines()
        verseListCombined = []
        for i in range(0, len(verseList), 2):
            verseListCombined.append(verseList[i] + ' ' + verseList[i+1])

        print('\n'+passage.get_text().strip())
        print(*verseListCombined)

# Init funcion
userInput()
