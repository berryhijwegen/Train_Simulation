import station_states

class Station(object):
    """ 
    A simple state machine that mimics the functionality of a device from a 
    high level.
    """

    def __init__(self, station_name, previous_station=None, next_station=None):
        """ Initialize the components. """

        # Start with a default state.
        self.station_name = station_name
        self.previous_station = previous_station
        self.next_station = next_station
        self.platforms = []

    def add_platform(self, platform):
        self.platforms.append(platform)

    def set_previous_station(self, station):
        self.previous_station = station

    def set_next_station(self, station):
        self.next_station = station

    def get_platform_by_num(self, num):
        for platform in self.platforms:
            if platform.platform_num == num:
                return platform
        return False

    def on_event(self, event):
        """
        This is the bread and butter of the state machine. Incoming events are
        delegated to the given states which then handle the event. The result is
        then assigned as the new state.
        """

        # The next state will be the result of the on_event function.
        self.state = self.state.on_event(event)

    def __str__(self):
        return f"Station {self.station_name}"

    def __repr__(self):
        return self.__str__()