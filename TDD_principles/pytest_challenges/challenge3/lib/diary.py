class DiaryEntry:
    def __init__(self, title, contents):
        if type(title) != str and type(contents) != str or len(title) == 0 and len(contents) == 0:
            raise Exception('Please check the contents or title.')
        else:
            self.title  = title
            self.contents = contents

    def format(self):
       return f'{self.title}: {self.contents}'
       
    def count_words(self):
        return len(self.contents)
       

    def reading_time(self, wpm):
        if type(wpm) == int:
            return round(len(self.contents) / wpm)
        else:
            raise Exception('Invalid input, input needs to be of type int.')


    def reading_chunk(self, wpm, minutes):
        if type(wpm) == int and type(minutes) == int:
            return (' ').join([word for word in self.contents.split(' ')][:wpm*minutes])
        else:
            raise Exception('Please input an integer')
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass
