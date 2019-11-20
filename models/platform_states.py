from state import State

# Start of our states
class EmptyState(State):
    """
    The state which indicates that there are limited device capabilities.
    """

    def on_event(self, event):
        if event == 'train_on_platform':
            return OccupiedState()

        return self


class OccupiedState(State):
    """
    The state which indicates that there are no limitations on device
    capabilities.
    """

    def on_event(self, event):
        if event == 'train_not_on_platform':
            return EmptyState()

        return self