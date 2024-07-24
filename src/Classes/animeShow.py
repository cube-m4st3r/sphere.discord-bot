from Classes.animeGenres import AnimeGenre
from Classes.animeThemes import AnimeTheme

class AnimeShow:
    def __init__(self, data: dict):
        show_data = data["anime_show"]
        self._id = show_data["id"]
        self._title = show_data["title"]
        self._type = show_data["type"]
        self._episodes_amount = show_data["eps_amount"]
        self._status = show_data["status"]
        self._aired_start = show_data["aired_start"]
        self._aired_end = show_data["aired_end"]
        self._premiered = show_data["premiered"]
        self._broadcast = show_data["broadcast"]
        self._source = show_data["source"]
        self._genre = [AnimeGenre(data=genre) for genre in data["genres"]]
        self._theme = [AnimeTheme(data=theme) for theme in data["themes"]]

    
    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def type(self):
        return self._type

    @property
    def episodes_amount(self):
        return self._episodes_amount

    @property
    def status(self):
        return self._status

    @property
    def aired_start(self):
        return self._aired_start

    @property
    def aired_end(self):
        return self._aired_end

    @property
    def premiered(self):
        return self._premiered

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def source(self):
        return self._source

    @property
    def genre(self):
        return self._genre

    @property
    def theme(self):
        return self._theme


    @id.setter
    def id(self, value):
        self._id = value

    @title.setter
    def title(self, value):
        self._title = value

    @type.setter
    def type(self, value):
        self._type = value

    @episodes_amount.setter
    def episodes_amount(self, value):
        self._episodes_amount = value

    @status.setter
    def status(self, value):
        self._status = value

    @aired_start.setter
    def aired_start(self, value):
        self._aired_start = value

    @aired_end.setter
    def aired_end(self, value):
        self._aired_end = value

    @premiered.setter
    def premiered(self, value):
        self._premiered = value

    @broadcast.setter
    def broadcast(self, value):
        self._broadcast = value

    @source.setter
    def source(self, value):
        self._source = value

    @genre.setter
    def genre(self, value):
        self._genre = AnimeGenre(data=value)

    @theme.setter
    def theme(self, value):
        self._theme = AnimeTheme(data=value)