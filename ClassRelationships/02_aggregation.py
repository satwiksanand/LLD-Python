# Aggregation is a type of relationship where there is a clear logical "whole-part" relationship between objects.
# It is also a "has-a" relationship, but it represents a stronger semantic relationship than a general association.
# The difference between association and aggregation can be understood through the relationship and hierarchy between
# the objects. In a normal association, the connected objects are generally independent and exist on an equal conceptual
# level. However, aggregation establishes a "whole-part" hierarchy, where one object represents the whole and contains
# or groups other objects as its parts.

# Despite this relationship, the lifecycle of both objects remains independent. The part objects can exist even if the
# whole object is destroyed. The key distinction is therefore not lifecycle dependency, but the existence of a meaningful
# whole-part relationship between the objects.

# In UML. aggregation is represented as a empty diamond solid line, diamond being on the "whole" object side.

# The Music Library Example:

# The entities of the program
# Library:-> It is the master collection of all the songs.
# Songs:-> the song entity
# Artist:-> singer who upload musics
# User:-> user of the music application who are able to make playlist and add songs to it.
# Playlist:-> collection of users according to their music taste.

# relationships between entities.

# Artist upload Songs -> this feels like association, because the Songs object are not tightly connected to the Artist Object
# technically the songs could remain in the master library even if the artist object were to be destroyed, now in case of association
# i am wondering what kind of association it is, first for the directional aspect, i believe it is bi-directional, since i would
# want to be able to figure out who the artist was, at the same time it would be great if the artist object is storing the all
# music made by it, so in that particular case, it seems bidirectional and multiplicity would be artist(1) ------> (0..*)songs

# songs are stored in master library -> this here it seems like composition, the lifecycle of the songs objects are tightly coupled
# with the master library, if the library were to be deleted in that case, the song objects would be destroyed as well

# user creates playlist -> users of the music application creates playlist, there are scenarios where when a user is deleted
# the playlist remains, but for this test case let's assume that deleting the user deletes his playlist as well, since the lifecycle
# of the playlist object is tightly coupled with the user object, we could say that this is composition.

# user adds songs to playlist -> the user is allowed to add different songs into their playlist, deleting the playlist doesn't
# delete the songs itself, so we could say that this is an example of aggregation

from enum import Enum

class PlaylistVisibility(Enum):
    PRIVATE = "PRIVATE"
    PUBLIC = "PUBLIC"

class MasterLibrary:
    @staticmethod
    def add_song(name: str, artist: "Artist", duration_in_seconds: int):
        return Song(name, artist, duration_in_seconds)


class Artist:
    def __init__(self, name: str):
        self._name = name
        self._songs: list[Song] = []

    def add_song(self, name: str, duration_in_seconds: int):
        self._songs.append(MasterLibrary.add_song(name, self, duration_in_seconds))

    def count(self):
        return len(self._songs)

    def list_songs(self):
        for song in self._songs:
            song.print_details()


class Song:
    def __init__(self, name: str, artist: Artist, duration_in_seconds: int):
        self._name = name
        self._artist = artist
        self._duration_in_seconds = duration_in_seconds

    def print_details(self):
        print(f"Song name: {self._name} and it lasts for {self._duration_in_seconds} seconds.")

class User:
    def __init__(self, name: str):
        self._name = name
        self._playlists: list[Playlist] = []

    def add_song_to_playlist(self, song: Song, index: int = -1):
        if 0 <= index < len(self._playlists):
            self._playlists[index].add_song(song)

class Playlist:
    def __init__(self, name: str, visibility: PlaylistVisibility):
        self.name = name
        self.visibility = visibility
        self.songs = []

    def add_song(self, song: Song):
        self.songs.append(song)

if __name__ == "__main__":
    artist = Artist("arijit")
    artist.add_song("ae dil hai mushkil", 12)
    artist.list_songs()