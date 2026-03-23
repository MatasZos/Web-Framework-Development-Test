import unittest
from PartA import Artist, Album, Song, Playlist

class TestMusicClasses(unittest.TestCase):
    def setUp(self):
        self.artist = Artist("Taylor Swift", "1989-12-13", "USA")
        self.album = Album("Fearless", "Taylor Swift", 2008)
        self.song = Song("Love Story", "Taylor Swift", 2008)
        self.playlist = Playlist("My Playlist")
