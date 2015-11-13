#!/usr/bin/python

from assumption import Assumption

class KilledBrackets(object):

  """
  A container object for all the brackets we do NOT need to account for, 
  given a certain list of assumptions
  """

  def __init__(self, *assumptions):
    self.Killedbrackets = []
    self.assumptions = assumptions
    self.makeKilledBrackets()


  def makeKilledBrackets(self):
    """
    Takes a list of assumption objects and initalizes or edits self.brackets
    to reflect the bracket we don't have to fill out
    """
    if not self.assumptions:
      return
    # Need to make the brackets here in the else case

  def howManyBrackets(self):
    """
    Returns the number of brackets we need to fill out, given the current
    state of assumptions
    """
    return (2 ** 63) - len(self.Killedbrackets)

  def addAssumption(self):

  # Will want getter and Setters for self.assumptions

if __name__ == '__main__':
  killed_brackets = KilledBrackets()
  print "Before any assumptions: {}".format(killed_brackets.howManyBrackets())

  ## Assume all 16s lose
  all_16s_lose = Assumption('All 16s Lose', {0: 0, 15:0, 30: 0, 45: 0})
  killed_brackets.addAssumption(all_16s_lose)
  print "After assuming all 16s lose: {}".format(killed_brackets.howManyBrackets())
