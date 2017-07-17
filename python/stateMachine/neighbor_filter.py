#!/usr/bin/env python
"""
"""

class NeighborFilter(object):
  """NeighborFilter is in charge of knowing whether two stations are neighbors, and if so which side they're on. """
  def __init__(self, station):
    super(NeighborFilter, self).__init__()
    self.id = station.id

  def IsLeftNeighbor(self, other):
    return other.id == self.id - 1 or other.id == 5 and self.id == 0

  def IsRightNeighbor(self, other):
    return other.id == self.id + 1 or other.id == 0 and self.id == 5


if __name__ == '__main__':
  # TODO(dunmatt): put some sort of test/example code here
  pass
