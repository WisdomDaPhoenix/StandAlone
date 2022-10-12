import requests
import pandas as pd
from pprint import pprint
source = input("Enter source or base currency: ").upper()
n = eval(input("How many output currencies do you like to see: "))
currencies = ""
for i in range(n):
  curr = input("Pls enter output currency: ").upper()+","
  currencies = currencies + curr
currencies = currencies[ :-1]
print(currencies)

url = f"https://api.apilayer.com/currency_data/live?source={source}&currencies={currencies}"

payload = {}
headers= {
  "apikey": "Xw3SK9l9Cl88sFLexTANbiAhK0A7Xs5T"
}
response = requests.request("GET", url, headers=headers, data = payload)
status_code = response.status_code
print(type(response.content))
result = response.json()
pprint(result)
print(result["quotes"])
others_vals = list(result["quotes"].values())
others_cur = [key[3:] for key in result["quotes"]]
# print(type(result["quotes"]))
print(others_cur)
print(others_vals)

ratestab = pd.DataFrame({
  "Currency":others_cur,
  "Rate":others_vals
})
ratestab.index = ratestab.index + 1
print(f"-------------RATES TABLE FOR {source.upper()}---------------")
print(ratestab)





# 0.97052
# 0.970926


