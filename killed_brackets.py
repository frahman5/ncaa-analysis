
class Killedbrackets(object):

  def __init__(self, *assumptions):
    self.Killedbrackets = []
    self.assumptions = assumptions
    self.makeBrackets(self.assumptions)


  def makeBrackets(self):
    """
    Takes a list of assumption objects and initalizes or edits self.brackets
    to reflect the bracket we'd have to fill out
    """



    # Need to make the brackets here

  def howManyBrackets(self):
    """
    Returns the number of brackets we need to fill out, given the current
    state of assumptions
    """
    return len(self.brackets)

  # Will want getter and Setters for self.assumptions