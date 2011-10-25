# ReadingTime

Calculate the approximate time required to read a string. By default it assumes a reading speed of 180 words per minute.

## Usage

**Basic usage**

    >>> from reading_time import ReadingTime
    >>> test_str = "The quick brown fox jumps over the lazy dog."
    >>> ReadingTime(test_str).how_long
    'not even a minute'

**Changing the WPM**

    >>> ReadingTime(test_str,1).how_long
    'about 9 minutes'
    >>> ReadingTime(test_str,9).how_long
    'about a minute'


**Why use `timedelta`?**

    >>> from datetime import datetime
    >>> now = datetime.now()
    >>> now
    datetime.datetime(2011, 10, 25, 16, 55, 41, 651553)
    >>> finished_reading = now + ReadingTime(test_str,1).duration()
    >>> finished_reading
    datetime.datetime(2011, 10, 25, 17, 4, 41, 651553)

## License

MIT: http://aaron.mit-license.org