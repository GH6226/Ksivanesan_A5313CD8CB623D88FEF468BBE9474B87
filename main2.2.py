class Player:
  def play(self):
     print("the player is playing cricket.")

#Define the derived class batsman
class Batsman(Player):
  def play(self):
     print("the batsman is batting.")

#Define the derived class bowler
class Bowler(Player):
  def play(self):
     print("the bowler is bowling.")

batsman=Batsman()
bowler=Bowler()

#call the play() method for each object.
batsman.play()
bowler.play()