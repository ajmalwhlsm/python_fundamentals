from pprint import pprint
import statistics
import requests
from collections import Counter
cat_api='https://api.thecatapi.com/v1/breeds'
def get_data_url(url):
    response=requests.get(url)
    content_type=response.headers.get("Content-Type","").lower()
    if 'application/json' in content_type:
        return response.json()
    elif 'text/' in content_type:
        return response.text
    else:
        return response.content
cats=get_data_url(cat_api)

weights=[]
lifespans=[]
countries=[]
for cat in cats:
    weight_range=cat['weight']['metric']
    low,high=weight_range.split("-")
    low=low.strip()
    high=high.strip()
    midrange=(float(low)+float(high))/2
    weights.append(midrange)
for cat in cats:
    lifespan_range=cat['life_span']
    low,high=lifespan_range.split("-")
    low=low.strip()
    high=high.strip()
    midrange=(float(low)+float(high))/2
    lifespans.append(midrange)

for cat in cats:
    countries.append(cat['origin'])
country_frequency=Counter(countries)
print("-------------Country Frequency-------------")
for country,frequency in country_frequency.items():
    print(country,"       |",frequency)
print("------------------------------------")
print("-------------Weights-------------")
print("Min:",min(weights))
print("Max:",max(weights))
print("Mean:",statistics.mean(weights))
print("Median:",statistics.median(weights))
print("Std:",statistics.stdev(weights))
print("----------------------------------")
print("-------------Lifespan-------------")
print("Min:",min(lifespans))
print("Max:",max(lifespans))
print("Mean:",statistics.mean(lifespans))
print("Median:",statistics.median(lifespans))
print("Std:",statistics.stdev(lifespans))
print("----------------------------------")
print("--------------------------")



