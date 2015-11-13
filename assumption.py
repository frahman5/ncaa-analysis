

class Assumption(object):

  def __init__(self, name, assumptions = {}):
    self.name = name
    self.assumptDict = assumptions

  def addAssumption(self, game_id, val):
    assert val in (0, 1)
    self.assumptDict[game_id] = val

  def printName(self):
    print self.name

  def getAssumptions(self):
    for key in self.assumptDict.keys():
      print "Team {} will win game {}".format(self.assumptDict[key], key)

if __name__ == '__main__':
  all_16s_lose = Assumption('All 16s Lose', {0: 0, 15:0, 30: 0, 45: 0})
  all_16s_lose.printName()
  all_16s_lose.getAssumptions()