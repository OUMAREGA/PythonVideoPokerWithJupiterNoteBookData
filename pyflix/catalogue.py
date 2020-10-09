
class TvShow:
    def __init__(self, title:str):
        self.title = title.capitalize()
        self._episodes = []

    def add_episode(self, season, number, title, duration, year):
        self._episodes.append({"title": title, "season": season, "number": number, "duration": duration, "year": year})

    def __str__(self):
        return f"{self.title} with {len(self._episodes)} episodes"

    def __eq__(self, other):  # self == other  <- ce que vous écrivez, python fait self.__eq__(other)
        if not isinstance(other, TvShow):
            return False

        return self.title == other.title

    @property
    def duration(self):
        return sum([episode['duration'] for episode in self._episodes])

    @property
    def episodes(self):
        return self._episodes.copy()

