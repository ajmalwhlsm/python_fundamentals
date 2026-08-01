def load_text(text):
    if text.endswith('.txt'):
        with open(text,'r') as f:
            return f.read()
    return text

def check_similarity(text1,text2):
    text1=set(load_text(text1).lower().split())
    text2=set(load_text(text2).lower().split())
    common=text1&text2
    similarity=(len(common)/len(text1))*100
    return similarity
    
     
print(check_similarity('michal_ospeech.txt','melinaspeech.txt'))