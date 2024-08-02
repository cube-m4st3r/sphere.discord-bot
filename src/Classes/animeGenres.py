class AnimeGenre:
    def __init__(self, data: dict):
        self._id = data["animegenre"]["id"] # fix soon
        self._name = data["animegenre"]["name"]

    def to_dict(self):
        return {
            "animegenre": {
                "id": self._id,
                "name": self._name
            }    
        }

    @staticmethod
    def from_dict(data):
        return AnimeGenre(data)

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @id.setter
    def id(self, value):
        self._id = value

    @name.setter
    def name(self, value):
        self._name = value