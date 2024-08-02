from Classes.animeGenres import AnimeGenre
from Classes.animeThemes import AnimeTheme
from datetime import datetime
import json

class AnimeShow:
    def __init__(self, data: dict):
        self._id = data["id"]
        self._title = data["title"]
        self._type = data["type"]
        self._episodes_amount = data["episodes_amount"]
        self._status = data["status"]
        self._aired_start = self._parse_date(data["aired_start"])
        self._aired_end = self._parse_date(data["aired_end"])
        self._premiered = data["premiered"]
        self._broadcast = data["broadcast"]
        self._source = data["source"]
        self._genre = [AnimeGenre(data=genre) for genre in data["animeshowgenres"]]
        self._theme = [AnimeTheme(data=theme) for theme in data["animeshowthemes"]]

    def _parse_date(self, date_str):
        try:
            return datetime.fromisoformat(date_str)
        except ValueError:
            return date_str

    def to_dict(self):
        return {
            "id": self._id,
            "title": self._title,
            "type": self._type,
            "episodes_amount": self._episodes_amount,  # Use camelCase for consistency with entity properties
            "status": self._status,
            "aired_start": self._aired_start.isoformat() if self._aired_start else None,  # Use ISO 8601 format
            "aired_end": self._aired_end.isoformat() if self._aired_end else None,  # Use ISO 8601 format
            "premiered": self._premiered,
            "broadcast": self._broadcast,
            "source": self._source,
            "animeshowgenres": [genre.to_dict() for genre in self._genre],
            "animeshowthemes": [theme.to_dict() for theme in self._theme]
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    @staticmethod
    def from_dict(data):
        return AnimeShow(data)

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        return AnimeShow.from_dict(data)
    
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