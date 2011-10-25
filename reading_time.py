from datetime import timedelta
import math


class ReadingTime:

    def __init__(self, text, wpm=180):
        self.words = text.split(" ")
        self.wpm = wpm
    
    def duration(self):
        minutes = math.floor(len(self.words) / self.wpm)
        
        return timedelta(minutes=minutes)
    
    def humanize(self):
        d = self.duration()
        
        if d < timedelta(minutes=1):
            return "not even a minute"
        elif d == timedelta(minutes=1):
            return "about a minute"
        elif d < timedelta(hours=1):
            return "about %s minutes" % int(math.floor(d.seconds / 60))
        elif d <= timedelta(hours=1, minutes=20):
            return "about an hour"
        else:
            return "some time"
    
    how_long = property(humanize)