from urllib.requests import urlopen
def fetch_words:
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words[]
        for line in story:
            line_words=line.decode('utf-8').split()
                for words in line_words:
                    story_words.append(words)
                      
    for words in story_words:
    print(words)

