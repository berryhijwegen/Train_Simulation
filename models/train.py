from train_states import StationaryState

class Train(object):
    """ 
    Train Class is responsible for starting and stopping itself. It keeps track on its state, its current station and the platform it's on.
    """

    def __init__(self, num, track, station):
        """ Initialize the Train. """

        # Start with a default state.
        self.track = track
        self.num = num
        self.state = StationaryState()
        self.current_station = station
        self.current_platform = self.track.available_platform(self.current_station)
        self.current_platform.on_event('train_on_platform')
        self.current_track = None
        self.moving_to = None

    def on_event(self, event, station=None):
        """
        This is the bread and butter of the state machine. Incoming events are
        delegated to the given states which then handle the event. The result is
        then assigned as the new state.
        """

        if event == 'starting':
            self.state = self.state.on_event(event)
            self.moving_to = station
            self.current_platform.on_event('train_not_on_platform')
            self.current_platform = None

        elif event == 'stopping':
            if self.track.available_platform(self.moving_to):
                self.state = self.state.on_event(event)
                self.current_station = self.moving_to
                self.current_platform = self.track.available_platform(self.moving_to)
                self.moving_to = None
                self.current_platform.on_event('train_on_platform')
            else:
                self.state = self.state.on_event('platform_occupied')
        else:
            self.state = self.state.on_event(event)

    def __str__(self):
        moving_string = f"Currently not moving. At Platform {self.current_platform.platform_num}." if not self.moving_to else f"Moving To Station = {self.moving_to}"
        return f"Current State = {self.state}, Current Station = {self.current_station}, {moving_string}"

    def __repr__(self):
        return self.__str__()
