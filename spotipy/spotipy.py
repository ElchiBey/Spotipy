from artist import Artist
from song import Song
from album import Album
from functools import *
from itertools import *


class SpotiPy:
    def __init__(self):
        self.__artists = []

    def getArtists(self):
        return self.__artists

    def addArtists(self, *artists):
        for artist in artists:
            if not self.__artists:
                self.__artists.append(artist)
            else:
                same = 0
                for art in self.__artists:
                    if artist.getFirstName() == art.getFirstName() and \
                         artist.getSecondName() == art.getSecondName() and \
                         artist.getBirthYear() == art.getBirthYear():
                        same += 1
                if same == 0:
                    self.__artists.append(artist)

    def getTopTrendingArtist(self):
        lst = sorted(self.getArtists(), key=lambda artist: artist.totalLikes())
        return lst[-1].getFirstName(), lst[-1].getSecondName()

    def allAlbums(self):
        albums = []
        for artist in self.__artists:
            for alb in artist.getAlbums():
                albums.append(alb)
        return albums

    def getTopTrendingAlbum(self):
        albums = self.allAlbums()
        popularAlbum = sorted(albums, key=(lambda alb: sum([song.getLikes() for song in alb.getSongs()])))[-1]
        return popularAlbum

    def getTopTrendingSong(self):
        allSingles = []
        for artist in self.__artists:
            allSingles.append(sorted(artist.getSingle(), key=lambda single: single.getLikes())[-1])
        for artist in self.__artists:
            for album in artist.getAlbums():
                allSingles.append(album.sortByPopularity(False)[0])

        if allSingles:
            return sorted(allSingles, key=lambda song: song.getLikes())[-1].getTitle()

    @staticmethod
    def loadFromFile(filePath):
        file = open(filePath, 'r')
        data = file.read()
        artistLst = data[7:].split("#")
        spoty = SpotiPy()
        for artist in artistLst:
            spoty.addArtists(Artist.helperArtist(artist))
        return spoty
