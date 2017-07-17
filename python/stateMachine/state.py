#!/usr/bin/env python
"""
"""

class State(object):
  """Base class for all states in the state machine."""
  def __init__(self, message_sender, neighbor_filter = None):
    super(State, self).__init__()
    self.sender = message_sender
    self.neighbor_filter = neighbor_filter or NeighborFilter()

  def OnEnter(self, previous):
    """This gets called when the previous state transitions to this one."""
    pass

  def OnLeaving(self, next):
    """This gets called immediately before leaving for another state."""
    pass

  def HandleInput(self, controls_state, network_message):
    """HandleInput takes the state of the physical controls and any message that may be incomming, acts, and returns the next state."""
    # TODO(dunmatt): overload this in child states
    pass

  def HandleControlsChanged(self, controls_state):
    """Handler for changes in the physical control.  Handles the input and sends an update to the other stations."""
    # TODO(dunmatt): use self.sender to send an update message
    self.HandleInput(controls_state, None)


if __name__ == '__main__':
  # TODO(dunmatt): put some sort of test/example code here
  pass
