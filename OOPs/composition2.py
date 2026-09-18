class Human:
    def emotions(self):
        print("Human Has its own emotions,")


class individual:
    def __init__(self) -> None:
        self.emotion = Human()

    def emotions(self):
        self.emotion.emotions()
        print("But But individual have their own feelings at partivular time")


objref = individual()
objref.emotions()
