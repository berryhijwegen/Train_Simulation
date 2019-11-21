from state import State

# States for Platform.py

class EmptyState(State):
    """
    The state which indicates that there is no train on the platform.
    """

    def on_event(self, event):
        if event == 'train_on_platform':
            return OccupiedState()

        return self


class OccupiedState(State):
    """
    The state which indicates that there is a train on the platform.
    """

    def on_event(self, event):
        if event == 'train_not_on_platform':
            return EmptyState()

        return self
