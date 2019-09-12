#!/usr/bin/env python3
""" This script is used to get the contents of any site and then split that into individual words"""
from urllib.request import urlopen
from sys import argv

def fetch_words(url):
    """ Gets words from URL
        
        Args-
        URL

        Returns-
        List of words
    """
    with urlopen(url) as story:
        story_words=[]
        for line in story:
            line_words=line.decode('utf-8').split()
            for words in line_words:
                    story_words.append(words)
    return story_words

def print_items(items) :                 
    for item in items:
        print(item)

def main(url):
    word=fetch_words(url)
    print_items(word)

if __name__ == "__main__":
    main(argv[1])

