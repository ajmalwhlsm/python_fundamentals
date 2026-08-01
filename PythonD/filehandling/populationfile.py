import json
def most_population(files,tophow):
  with open(files,'r',encoding='utf-8') as f:
    dct=json.load(f)
  c_p={}
  for country in dct:
    c_p[country['name']]=country['population']
    
  sorted_population=sorted(c_p.items(),key=lambda x:x[1],reverse=True)
  return(sorted_population[:tophow])

      
    
print(most_population('countries_data.json',10))