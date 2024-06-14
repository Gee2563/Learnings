# File: lib/track.py

class Track:
    def __init__(self, title, artist):
        if type(artist) == str and type(title) == str:
            self.artist = artist
            self.title = title
        else :
            raise Exception('Invalid input')
  

    def matches(self, keyword):
        if type(keyword) == str:
            return keyword in self.title
        else:
            raise Exception('Invalid input')
        # keyword is a string
        # Returns true if the keyword matches either the title or artist
        pass
