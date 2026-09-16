class Engine:
    def start(self):
        print("Engine Started,")


class Car:
    def __init__(self) -> None:
        self.engine = Engine()

    def car_start(self):
        self.engine.start()
        print("now car has started")


objref = Car()
objref.car_start()
