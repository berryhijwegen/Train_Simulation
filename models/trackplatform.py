from platform_states import EmptyState

class Platform(object):
    """ 
    A Platform is part of a station. A Station can have multiple Platforms. A Platform can have one Station. On every platform there can be one Train.
    """

    def __init__(self, num):
        """ Initialize the components. """

        # Start with a default state.
        self.state = EmptyState()
        self.platform_num = num

    def on_event(self, event):
        """
        This is the bread and butter of the state machine. Incoming events are
        delegated to the given states which then handle the event. The result is
        then assigned as the new state.
        """

        # The next state will be the result of the on_event function.
        self.state = self.state.on_event(event)

    def __str__(self):
        return f"Platform {self.platform_num} is currently {'empty' if isinstance(self.state, EmptyState) else 'occupied'}."

    def __repr__(self):
        return self.__str__