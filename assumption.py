#! /usr/bin/python
from CONFIG import *

class Assumption(object):

  def __init__(self, assumption_file):
    self.name = None
    self.conditions = []
    self.load(assumption_file)
    assert self.name

  def load(self, assumption_file):
    with open(assumption_file, 'r') as f:

      # Get lines
      all_lines = list(f)
      assert self._checkFormating(assumption_file, all_lines)

      # Set name
      self.name = all_lines[1].replace('\n', "")

      # Set conditions
      end_index = self._get_end_index(all_lines)
      for condition_string in all_lines[3:end_index]:
        self.conditions.append(self._string_to_tuple(condition_string))

  def _checkFormating(self, assumption_file,  file_lines):
    general_error = "File {} does not have proper formatting.".format(assumption_file)
    name_error = "Line 0 must be # Name"
    conditions_error = "Line 2 must be # Conditions"
    end_error = "File must end with # End"
    assert file_lines[0].startswith('# Name'), "{}, **{}**".format(general_error, name_error)
    assert file_lines[2].startswith('# Conditions'), "{} **{}**".format(general_error, conditions_error)
    assert file_lines[-1].startswith('# End') or file_lines[-1] == '\n'

    return True

  def _string_to_tuple(self, string):
    # Container for duples
    listy_tuple = []

    # Break the line down into component duple strings and convert them to duples
    all_duple_strings = string.split(";")
    for duple_string in all_duple_strings:
        x = duple_string.replace('(',"").replace(')',"").split(",")
        listy_tuple.append((int(x[0]), int(x[1])))

    return tuple(listy_tuple)

  def _get_end_index(self, file_lines):
    i = 0

    # find the end line
    for line in file_lines:
      if line.find('# End') >= 0:
        break
      i += 1

    # make sure there was an end line if we got to the end of the file
    if i == len(file_lines):
      assert line.find('# End') >= 0

    return i

  def printself(self):
    print self.name
    for c in self.conditions:
      print c

if __name__ == '__main__':
  all_16s_win = Assumption(DATA + '/assumption1.txt')
  all_16s_win.printself()
  assumption2 = Assumption(DATA + '/assumption2.txt')
  assumption2.printself()
  assumption3 = Assumption(DATA + '/assumption3.txt')
  assumption3.printself()