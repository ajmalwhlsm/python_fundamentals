import json
def most_spoken_languages(files,tophow):
  with open(files,'r',encoding='utf-8') as f:
    dct=json.load(f)
  language_count={}
  for country in dct:
    for language in country['languages']:
      if language in language_count:
        language_count[language]+=1
      else:
        language_count[language]=1
  sorted_lang=sorted(language_count.items(),key=lambda x:x[1],reverse=True)
  return(sorted_lang[:tophow])
print(most_spoken_languages('countries_data.json',10))