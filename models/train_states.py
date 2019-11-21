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
        elif event == 'platform_occupied':
            return WaitingState()
        return self

class WaitingState(State):
    def on_event(self, event):
        if event == 'platform_empty':
            return StationaryState()
        return self