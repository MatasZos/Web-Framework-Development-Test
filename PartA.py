
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
        



class Album:
    def __init__(self, title, artist_name, year):
        self.title = title
        self.artist_name = artist_name
        self.year = year
        self.songs = [] 
        
    def add_song(self,title,year):
        new_song=Song(title,self.artist_name,year)
        self.songs.append(new_song)
        return new_song
    
    
    def display_info(self):
        print("Title of album:", self.title)
        print("Artist that made it:", self.artist_name)
        print("Year it was released:", self.year)
        print("Songs in the album:")
        for song in self.songs:
            print("  -", song.title, "(", song.year, ")")
        print("_" * 40)

    
class Song:
    def __init__(self, title,artist_name, year):
        self.title = title
        self.artist_name = artist_name
        self.year = year
        
    def display_info(self):
        print("Title of song:", self.title)
        print("Artist that made it:", self.artist_name)
        print("Year it was released:", self.year)
        print("_" * 40)



class Playlist:
    def __init__(self, title):
        self.title = title
        self.songs = [] 
        
    
    def print_all_songs(self):
        print("Name of Playlisy:", self.title)
        if not self.songs:
            print("No songs found")
        else:
            """index list"""
            for i, song in enumerate(self.songs, start=1):
                print(f"{i}.{song.title}-{song.artist_name}({song.year})")
        print("_" * 40)
