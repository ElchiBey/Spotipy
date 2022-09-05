from song import Song
from album import Album


class Artist:
    def __init__(self, firstName, lastName, birthYear, albums, singles):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__birthYear = birthYear
        self.__albums = albums
        self.__singles = singles

    def getFirstName(self):
        return self.__firstName

    def getSecondName(self):
        return self.__lastName

    def getBirthYear(self):
        return self.__birthYear

    def getAlbums(self):
        return self.__albums

    def getSingle(self):
        return self.__singles

    def mostLikedSong(self):
        sngs = []
        for album in self.__albums:
            for song in album.getSongs():
                sngs.append(song)
        for song in self.__singles:
            sngs.append(song)
        return sorted(sngs, key=lambda songs: songs.getLikes())[-1]

    def leastLikedSong(self):
        sngs = []
        for album in self.__albums:
            for song in album.getSongs():
                sngs.append(song)
        for song in self.__singles:
            sngs.append(song)
        return sorted(sngs, key=lambda songs: songs.getLikes())[0]

    def totalLikes(self):
        sngs = []
        for album in self.__albums:
            for song in album.getSongs():
                sngs.append(song)
        for song in self.__singles:
            sngs.append(song)
        total = 0
        for song in sngs:
            total += song.getLikes()
        return total

    def __str__(self):
        return f'Name: {self.__firstName} {self.__lastName},Birth year:{self.__birthYear},Total likes:{self.totalLikes()}'

    @classmethod
    def helperArtist(cls, txt):
        txt = txt.strip(" :}{\n")
        artist, first = txt.split("albums:")
        albums, singles = first.split("},")
        albms = []
        sngls = []
        for album in albums.split("%"):
            albms.append(Album.helperAlbum(album))
        singles = singles.strip(" \n")
        for single in singles[7:].split("|"):
            sngls.append(Song.helperSong(single))
        artist = artist.strip(" ,\n}{:")
        fName, lName, birthYear = artist.split(",")
        return Artist(fName, lName, birthYear, albms, sngls)
