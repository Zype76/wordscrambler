#!/usr/bin/python3
import random

def jumbles():
        word = input("What's the word? ")
        listword = list(word)
        long = len(word)
        letterlist = []
        while 0 < long:
                lol = random.randint(0,long)
                letterlist.append(listword[lol-1])
                del listword[lol-1]
                long = long-1
        print(''.join(letterlist))

jumbles()
