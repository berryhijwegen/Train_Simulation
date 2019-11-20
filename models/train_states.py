from state import State

# Start of our states
class StationaryState(State):
    def on_event(self, event):
        if event == 'starting':
            return MovingState()
        return self


class MovingState(State):
    def on_event(self, event):
        if event == 'stopping':
            return StationaryState()

        return self