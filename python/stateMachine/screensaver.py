#!/usr/bin/env python
"""
"""

class Screensaver(State):
  """This is the state when nobody is in or near the structure."""
  def __init__(self, message_sender, neighbor_filter = None):
    super(Screensaver, self).__init__(message_sender, neighbor_filter)
    # TODO(dunmatt): create the next states

  def HandleInput(self, controls_state, network_message):
    """HandleInput takes the state of the physical controls and any message that may be incomming, acts, and returns the next state."""
    # TODO(dunmatt): do something
    pass


if __name__ == '__main__':
  # TODO(dunmatt): put some sort of test/example code here
  pass

