from datetime import datetime, time
from platform_states import EmptyState, OccupiedState

class Track(object):
    """ 
    A simple state machine that mimics the functionality of a device from a 
    high level.
    """

    def __init__(self):
        """ Initialize the components. """
        # Start with a default state.
        self.trains = []
        self.stations = []
        self.timestamp = datetime(2020, 1, 1, 6, 0, 0)
    
    def add_train(self, train):
        self.trains.append(train)

    def add_station(self, station):
        if type(station) == list:
            for s in station:
                self.stations.append(s)
        else:
            self.stations.append(s)

    def alter_time_by_minutes(self, minutes):
        self.timestamp += time(0, minutes, 0)
        
    def available_platform(self, station):
        for platform in station.platforms:
            if isinstance(platform.state, EmptyState):
                platform.state == OccupiedState()
                return platform
        
        return False

    def platform_on_event(self, station, platform_num, event):
        platform = station.get_platform_by_num(platform_num)
        platform.state = platform.on_event(event)