class Encounter:

    def __init__(self,name,kind):
        self.name = name
        self.type = type(kind)
        self.info = kind

    def init(self):
        return self.info

