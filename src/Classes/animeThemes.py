class AnimeTheme:
    def __init__(self, data: dict):
        self._id = data["animethemes"]["id"] # fix soon
        self._name = data["animethemes"]["name"]

    def to_dict(self):
        return {
            "animethemes": {
                "id": self._id,
                "name": self._name
            }   
        }

    @staticmethod
    def from_dict(data):
        return AnimeTheme(data)

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