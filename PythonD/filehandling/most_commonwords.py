import nltk
import string
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def find_most_common_words(text,tophow,remove_stop=False):
    with open(text,'r') as f:
        common_words={}
        for line in f:
          words=line.split()

          
          for word in words:
             word=word.lower().strip(string.punctuation)
             if remove_stop and word in stop_words:
                continue 
             if word in common_words:
                common_words[word]+=1
             else:
                common_words[word]=1
    top_words=sorted(common_words.items(),key=lambda x:x[1],reverse=True)
    return(top_words[:tophow])
               


print(find_most_common_words('romeo_and_juliet.txt',10,True))

