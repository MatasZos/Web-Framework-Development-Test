import unittest
from PartA import Artist, Album, Song, Playlist

class TestMusicClasses(unittest.TestCase):
    def setUp(self):
        self.artist = Artist("Taylor Swift", "1989-12-13", "USA")
        self.album = Album("Fearless", "Taylor Swift", 2008)
        self.song = Song("Love Story", "Taylor Swift", 2008)
        self.playlist = Playlist("My Playlist")

    """unit test for if an object is an instance of a class"""
    def test_artist_instance(self):
        self.assertIsInstance(self.artist, Artist)

    def test_album_instance(self):
        self.assertIsInstance(self.album, Album)

    def test_song_instance(self):
        self.assertIsInstance(self.song, Song)

    def test_playlist_instance(self):
        self.assertIsInstance(self.playlist, Playlist)
