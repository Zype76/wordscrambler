#!/usr/bin/python3
import random 

def jumbles(): 
	word = input("What's the word? ")
	listword = list(word)
	long = len(word)
	letterlist = [] 
	for x in range(0, len(word)):
		lol = random.randint(0,len(word) )
		letterlist.append(listword[lol-1])
	print(''.join(letterlist))

jumbles()
