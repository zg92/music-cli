import random

class verse_generator:
    # def __init__(self):
        
    def get_lyrics(self): 
        with open('verse.txt', 'r') as fp:
            return fp.read().split('\n\n')

    def lyrics(self, verse_count):
        lyric_list = self.get_lyrics()
        random_lyrics = [lyric_list[random.randint(0,len(lyric_list))] for i in range(int(verse_count))]
        self.display_lyrics(random_lyrics)

    def display_lyrics(self, lyrics):
        for verse in lyrics:
            print(verse)
            print('\n')


