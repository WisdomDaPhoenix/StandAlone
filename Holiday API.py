import requests
from pprint import pprint
myapi = "1f35009cb186481bb5c3b7d9ee794ba3"
url = "https://holidays.abstractapi.com/v1/?"
country = input("Which country: ")
year = input("What year: ")
month = input("Month: ")
day = input("Day in month: ")
response = requests.get(f"{url}api_key={myapi}&country={country}&year={year}&month={month}&day={day}")
# response = requests.get(f"{url}api_key={myapi}&country={country}")

print(response.status_code)
pprint(response.json())


