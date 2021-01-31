import pandas as pd
from bs4 import BeautifulSoup
import requests


url = "https://www.konga.com/"
homepage = requests.get(url)
pagesoup = BeautifulSoup(homepage.content, 'html.parser')
maindealstable = pagesoup.find(class_= "b49ee_2pjyI")
dealItems = maindealstable.find_all(class_="_25677_1VXsu")
dealItemstext = [item.text[:-3] for item in dealItems]
pricecontainer = maindealstable.find_all(class_="bbe45_3oExY f3ae7_36n5H")

rawpricelist = [item.find(class_='_4e81a_39Ehs f57ef_hFN-_') for item in pricecontainer]

pricelist = [item.find(class_='d7c0f_sJAqi').get_text() for item in rawpricelist]
pricelist = [item[1:] for item in pricelist]

pricelist = ['NGN'+item for item in pricelist]



dealstable = pd.DataFrame(
    {
        "Items": dealItemstext,
        "Prices": pricelist

    })
print(dealstable)
import os
if os.path.exists("kongadealstoday.csv"):
  os.remove("kongadealstoday.csv")
  dealstable.to_csv('kongadealstoday.csv')
  print("Your konga deals file is ready")
else:
  dealstable.to_csv('kongadealstoday.csv')
  print("Your konga deals file is ready")


