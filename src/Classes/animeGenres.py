class AnimeGenre:
    def __init__(self, data: dict):
        self._id = "N/A" # fix soon
        self._name = data

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