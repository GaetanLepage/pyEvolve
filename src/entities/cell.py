class Cell:

    def __init__(self, ipos, jpos, state=0):
        self.state = 0
        self.ipos = ipos
        self.jpos = jpos

    def die(self):
        self.state = 0

    def live(self):
        self.state = 1
