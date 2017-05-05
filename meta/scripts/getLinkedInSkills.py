#!/usr/bin/env python

from bs4 import BeautifulSoup
import csv
import json
import os
import requests
import sys

#cwd = os.getcwd()  # Get the current working directory (cwd)
#files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in '%s': %s" % (cwd, files))

#URI of the data source
URI = sys.argv[1] if len(sys.argv) > 1 else 'https://www.linkedin.com/in/jasclark/'

def parse_source(uri):
    request = requests.get(uri, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    #request = requests.get(uri, headers={'User-Agent' : 'jasonclark.info indexing bot'})

    #check for HTTP codes other than 200
    if request.status_code != 200:
        print('Status:', request.status_code, 'Problem with the request. Exiting.')
        exit()

    soup = BeautifulSoup(request.text, 'html.parser')
    #soup = BeautifulSoup(request, 'html.parser')
    #print soup.findAll('a')
    #print soup.prettify()
    #print(soup.get_text())

    pageTitle = soup.title.string
    pageFileName = pageTitle.replace(' ', '-').lower()
    #personName = soup.select(".pv-top-card-section__name")
    #personFileName = personName.replace(' ', '-')

    print ('Page Title: \n' + pageTitle)
    #print ('Person: \n' + personName)
    print ('Page URL: \n' + uri)

    #set empty list for about json values
    skillList = [] 

    for link in soup.find_all(class_='skill'):
    #alternative class name for full linkedin pageview 
    #for link in soup.find_all(class_='pv-skill-entity__skill-name'):
        tagValue = link.string.strip('\r\n\t')
        print('skill data: \n' + tagValue)
        skillList.append({"skill": tagValue, "length": len(tagValue)})
    
    #create json file if it doesn't exist, open and write parsed values into it
    if not os.path.exists(pageTitle+'-skills.json'):
        open(pageFileName+'-skills.json', 'w').close()
    
    with open(pageFileName+'-skills.json', 'r+') as jsonFile:
        json.dump(skillList, jsonFile, indent = 4)

    jsonFile.close()

    #create csv file if it doesn't exist, open and write parsed values into it
    if not os.path.exists(pageTitle+'-skills.csv'):
        open(pageFileName+'-skills.csv', 'w').close()

    with open(pageFileName+'-skills.csv', 'r+') as csvFile:
        writeFile = csv.writer(csvFile)
        writeFile.writerow(skillList)

    csvFile.close()

showResult = parse_source(URI)
print showResult
print 'JSON and CSV files created.'
