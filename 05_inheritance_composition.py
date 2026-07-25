class Marvel:
    def __init__(self, power):
        self.power = power

    def superhero(self):
        print("Thor has {self.power} asgaurd....")

class doomsday(Marvel):
    def in_movie(self):
        print("Thor will return in Doomsday")

M1 = Marvel()
M1.superhero()