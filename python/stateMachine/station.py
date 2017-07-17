#!/usr/bin/env python
"""
"""

class Station(object):
  """A Station is one of the six controllable units of the House of Enlightenment."""
  def __init__(self, id, message_sender):
    super(Station, self).__init__()
    self.id = id
    self.state = Screensaver(message_sender)

  def ReadHardware(self):
    """Reads the state of this station's physical controls and returns a controls_state object."""
    # TODO(dunmatt): write me
    return None


if __name__ == '__main__':
  # TODO(dunmatt): put some sort of test/example code here
  pass
