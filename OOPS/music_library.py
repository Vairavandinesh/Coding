import random
#Write a Python program to create a class called "MusicLibrary" with a 
# collection of songs and methods to add and remove songs, and to play a random song.
#requirements
# attributes : songs,artists
#methods : add songs,remove songs,play a random song
class MusicLibrary:
    def __init__(self):
        self.dicty={}
    def addsongs(self,song,artist):
        self.dicty[song]=artist
    def removesongs(self,song,artist):
        if song in self.dicty:
            self.dicty.pop(song)
    def playsong(self):
        song=random.choice(list(self.dicty.keys()))
        print(f"Playing {song} by {self.dicty[song]}")
library = MusicLibrary()

library.addsongs("Shape of You", "Ed Sheeran")
library.addsongs("Believer", "Imagine Dragons")
library.addsongs("Blinding Lights", "The Weeknd")
library.addsongs("Senorita", "Shawn Mendes")
library.addsongs("Perfect", "Ed Sheeran")

library.playsong()


