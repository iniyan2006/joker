#import csv
#import random
import requests

#joke = []
#with open("shortjokes.csv") as csv_file:
#	jokes = csv.reader(csv_file)
#	next(jokes)
#	for line in jokes:
#		joke.append(line[1])

def text():
  joker = requests.get('https://icanhazdadjoke.com/slack').json()
  jk = joker["attachments"][0]
  return jk["text"]
  
#print(text())
	
	

