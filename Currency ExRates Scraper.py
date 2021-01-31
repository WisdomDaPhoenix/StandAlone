from bs4 import BeautifulSoup
import pandas as pd
import requests



url = "https://www.iban.com/exchange-rates"
ratespage = requests.get(url)
pagesoup = BeautifulSoup(ratespage.content, 'html.parser')
maintable = pagesoup.find(class_='table')
innertable = maintable.find('tbody')
x = innertable.findChildren('img')
currencies = [img['alt'] for img in x]
fullvalueslist = innertable.findChildren('strong')
cur_values = [item.text for item in fullvalueslist]
print("Exchange rate to 1 Euro Today")

rates = pd.DataFrame(
    {
        "Currencies": currencies,
        "Value to 1 Euro": cur_values

    })
print(rates)









