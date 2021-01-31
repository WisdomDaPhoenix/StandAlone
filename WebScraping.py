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
----------------------------------------------------------------------------------------------------------------
IMPORTANT NOTES:
Platform specific installation notes
Windows
Though it’s possible to install Scrapy on Windows using pip, we recommend you to install Anaconda or Miniconda
and use the package from the conda-forge channel, which will avoid most installation issues. Installing scrapy using
pip makes you run into various technical installation issues.

Once you’ve installed Anaconda or Miniconda, open the command line on Anaconda program and install Scrapy using
the following command:
------------------------------------
conda install -c conda-forge scrapy
------------------------------------
Useful Scrapy commands:
fetch    ----- fetches URL using Scrapy downloader
genspider ----- generates new spider
runspider ----- run a spider
settings --------get settings values
shell ----------- open interactive scraping console
startproject ----- create new project
version ----- scrapy version
view  ------open URL in browser, as seen by Scrapy
-----------------------------------------------------------------------------------------
GETTING STARTED: SCRAPING A PAGE WITH SCRAPY

*CREATE PROJECT* - this creates a project directory
Command: scrapy startproject projectname

*CD PROJECTDIRECTORY/PROJECTDIRECTORY/SPIDERS* - this takes you to the spiders directory to create or generate
a spider
Command: scrapy genspider spidername domaintospider
e.g scrapy genspider sportnews goal.com

*RUN SPIDER* - this runs a spider using its default python filename
Command: scrapy runspider spiderfilename.py

*NAVIGATING TO A TAG ON XPATH* - this takes you directly to a html tag without passing through all containers on
the path to the tag. h1 tag for instance path can be - html/body/div/h1
//h1 - selects all h1 tags on the page
//div/h1 - selects only h1 tags that are immediate children of a div tag
//div//h1 - selects any h1 tag in a div tag whether its an immediate child or sub
//span[@class="title"] - selects any span tags that have the class attribute "title"
//span[@class="title"]/@id - selects the value of the id attribute where the class attribute is "title"



"""
from bs4 import BeautifulSoup
import requests
url = "https://www.tutorialspoint.com/index.htm"
req = requests.get(url)
scraped_data= BeautifulSoup(req.text, "html.parser")
print(scraped_data.title)
for link in scraped_data.find_all('a'):
    print(link.get('href'))
