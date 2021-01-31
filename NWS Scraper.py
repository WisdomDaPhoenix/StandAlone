"""
Web Scraping also known as Screen sraping, Web harvesting, Web crawling, Spiders or spidering
Moving across web pages via links
Scraping data from a single page, crawling across multiple pages to get data from each one.
For course purpose:
SCRAPING - FROM SINGLE PAGE
CRAWLING - FROM PAGE TO PAGE
BOTS - AUTOMATED INTERACTION WITH WEBSITES FOR WEB APPLICATIONS
Interactions with the websites with the goal of scraping data or with the goal of crawling from page to page.
The Bot performs the interactions.
A Web Scraper is a program that requests and parses any data on the web, especially in an unexpected way
Examples:
    A crawler that scans medical patient message boards looking for experiences with drug combinations
    Automated UI testing of a company's app
    A bot that interacts with an airline flight search app, monitoring price changes
INTERNET LAYERS:
Physical Layer: Wires
Data Link: MAC addreses and physical machines on a local network
Network: Creates network IP addresses, packets
Transport: Persistent communication channels, TCP, IP, PORTS
Session: Open, close, manage session, SCP
Presentation: String encoding, encryption, decryption, object serialization, files, compression
Application: HTTP, POST and GET requests REST APIs
Each request goes through many layers of wrapping and unwrapping to get to its destination and back
Requests do not require a web browser
Requests can be replicated and saved

"""
# print(week) ---- PRINTS ALL ITEMS IN THE DIV CALLED SEVEN-DAY-FORCAST-BODY
# print(soup) ---- PRINTS ALL HTML CONTENT ON THE PAGE, THE ENTIRE PAGE
# print(soup.find_all('a')) --- PRINTS ALL LINKS ON THE PAGE
# print(soup.find_all('li')) --- PRINTS ALL LIST ITEMS ON THE PAGE
import pandas as pd
import requests
from bs4 import BeautifulSoup


page = requests.get("https://forecast.weather.gov/MapClick.php?lat=34.1014&lon=-118.3359#.YAm1PehKjIU")
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id= 'seven-day-forecast-body')
items = week.find_all(class_='tombstone-container')
print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

#print(period_names)
#print(short_descriptions)
#print(temperatures)

weather_stuff = pd.DataFrame(
    {
    'period': period_names,
    'short-descriptions': short_descriptions,
    'temperatures' : temperatures
    })

print(weather_stuff)
weather_stuff.to_csv('weather_forcast.csv')



