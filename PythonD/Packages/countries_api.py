from pprint import pprint 
from helper import get_data_url
url="https://countries.dev/countries"

countries=get_data_url(url)

print("+++++++++++++++++++++++++++++++++++++")

print("---------------area top 10-----------------")
top_10_size=sorted(countries,key=lambda country:country.get("area",0),reverse=True)[:10]
for country in top_10_size:
    print(country["name"],country["area"])




language_count={}
for country in countries:
    for language in country["languages"]:
        language_name=language["name"]


        if language_name not in language_count:
            language_count[language_name]=1
        else:
            language_count[language_name]+=1
top10_lang=sorted(language_count.items(),key=lambda x:x[1],reverse=True)[:10]
print("---------------language top 10-----------------")
for language,count in top10_lang:
    print(language,count)

print("---------------Total languages-----------------")

languages_total=set()
for country in countries:
    for language in country['languages']:
        languages_total.add(language["name"])
print(len(languages_total))
print("+++++++++++++++++++++++++++++++++++++") 

        