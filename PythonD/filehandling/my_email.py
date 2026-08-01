import json

def email_extraction(file):
    with open(file,'r') as f:
        emails=[]
        for line in f:
            if line.startswith("From"):
                words=line.split()
                emails.append(words[1])
    return(emails)

print(email_extraction("email_exchanges_big.txt"))
        

