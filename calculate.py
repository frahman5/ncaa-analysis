#! /usr/bin/python

from CONFIG import *

from assumption import Assumption

def howManyBrackets(*assumptions):
  # Combine all Assumptions into one set of open brackets
  open_brackets = condenseAssumptions(*assumptions)

  # Calculate the number of possible brackets
  num_brackets = 0
  for ob in open_brackets:
    num_fixed_games = len(ob)
    num_brackets += (2 ** (63 - num_fixed_games))
  return num_brackets


def condenseAssumptions(*assumptions):
  if len(assumptions) == 1:
    return assumptions[0].getConditions()

  games_fixed = set()
  open_brackets = []
  for index, a in enumerate(assumptions):
      new_open_brackets = []

      ## If it's the first assumption, record the conditions and fixed games
      if index == 0:
        new_open_brackets = [ob for ob in a.getConditions()]

      ## Otherwise, check to see that no games clash, then add the new conditions
      else:
          assert len(games_fixed.intersection(a.getGamesFixed())) == 0, "Rule {} clashes with a previous rule".format(a.getName())
          for ob in open_brackets:
            for c in a.getConditions():
              new_open_brackets.append(tuple(list(ob) + list(c)))

      # Update the fixed games count and return
      games_fixed.update(a.getGamesFixed())
      open_brackets = new_open_brackets
  
  return open_brackets

def putBracketsNumberInPerspective(num_brackets):
    import math
    below = int(math.floor(math.log(num_brackets, 2)))
    above = int(math.ceil(math.log(num_brackets, 2)))
    return "(2^{}) < {} < (2^{})".format(below, num_brackets, above)


if __name__ == '__main__':
  import os
  nb = howManyBrackets(*[Assumption(DATA + '/' + a_file) for a_file in os.listdir(DATA))
  print putBracketsNumberInPerspective(nb)