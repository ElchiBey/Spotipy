from song import Song

class Album:
    def __init__(self, title, releaseYear):
        self.__title = title
        self.__releaseYear = releaseYear
        self.__songs = []

    def getTitle(self):
        return self.__title

    def getReleaseYear(self):
        return self.__releaseYear

    def getSongs(self):
        return self.__songs

    def addSongs(self, *songs):
        count = 0
        for song in songs:
            if not self.__songs:
                self.__songs.append(song)
                count += 1
            else:
                same = 0
                for album in self.__songs:
                    if song.getTitle() == album.getTitle() and \
                            song.getReleaseYear() == album.getReleaseYear() and \
                            song.getDuration() == album.getDuration():
                        same += 1
                        break
                if same == 0:
                    self.__songs.append(song)
                    count += 1
        return count

    def sortBy(self, byKey, reverse):
        return sorted(self.__songs, key=byKey, reverse=not bool(reverse))

    def sortByName(self, reverse):
        return Album.sortBy(self, lambda song: song.getTitle(), reverse)

    def sortByPopularity(self, reverse):
        return Album.sortBy(self, lambda song: song.getLikes(), reverse)

    def sortByDuration(self, reverse):
        return Album.sortBy(self, lambda song: song.getDuration(), reverse)

    def sortByReleaseYear(self, reverse):
        return Album.sortBy(self, lambda song: song.getReleaseYear(), reverse)

    def __str__(self):
        str = f'Title:{self.__title},Release year:{self.__releaseYear},songs:'
        str += '{'
        for i in range(len(self.__songs)):
            if not i == len(self.__songs) - 1:
                str += self.__songs[i].__str__() + '|'
            else:
                str += self.__songs[i].__str__()
        str += '}'
        return str

    @classmethod
    def helperAlbum(cls, txt):
        txt = txt.strip(" }{:\n")
        album, songs = txt.split("{")
        title, year, str = album.split(",")
        alb = Album(title, int(year))
        for song in songs.split("|"):
            alb.addSongs(Song.helperSong(song))
        return alb
