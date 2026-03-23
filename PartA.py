
import random


class Artist:
    def __init__(self, name, dob, country):
        self.name = name
        self.dob = dob
        self.country = country
        self.albums = []    
        self.songs = []
        
    def display_info(self):
        print("Artist name is:", self.name)
        print("Date of birth is:", self.dob)
        print("Country:", self.country)
        print("Albums made:")
        for album in self.albums:
            print(" , ", album.title)
        print("Songs made:")
        for song in self.songs:
            print(" , ", song.title)
        print("-"*40)
    
    def add_album(self,album):
        self.albums.append(self.album)
    
    def add_song(self,song):
        self.songs.append(song)

