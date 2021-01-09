def moveforward(self, distance):
    self.addHistory(("forward",distance))
    self.r1.moveforward(distance)
    self.r2.movebackward(distance)
def movebackward(self, distance):
    self.addHistory(("backward",distance))
    self.r1.movebackward(distance)
    self.r2.moveforward(distance)
def turnright(self):
    super().turnright()
    self.r1.turnright()
    self.r2.turnleft()
def turnleft(self):
    super().turnleft()
    self.r1.turnleft()
    self.r2.turnright()
def unplay(self) :
    super().unplay()
    self.r1.unplay()
    self.r2.unplay()
