import requests
import string
urlrao="https://www.gutenberg.org/cache/epub/1112/pg1112.txt"
def get_text(url):   
        response=requests.get(url)
        content_type=response.headers.get("Content-type","").lower()
        print(content_type)
        return response.text 
def get_top10(url,tophow=10):
        txt=get_text(url)
        counts={}
        words=txt.lower().split()
        
        for word in words:
          word=word.strip(string.punctuation)
          if word not in counts:
              counts[word]=1
          else:
              counts[word]+=1  
        sorted_words=sorted(counts.items(),key=lambda x:x[1],reverse=True)
        return sorted_words[:tophow]


get_text(urlrao)