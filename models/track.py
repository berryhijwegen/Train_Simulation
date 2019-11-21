from datetime import datetime, time
from platform_states import EmptyState, OccupiedState

class Track(object):
    """ 
    Class Track keeps track of all trains and stations on the particular track.
    """

    def __init__(self):
        """ Initialize the Track. """
        # Start with a default state.
        self.trains = []
        self.stations = []
    
    def add_train(self, train):
        """
        Add one (or multiple) train(s) to the track.
        """
        if type(train) == list:
            for t in train:
                self.trains.append(t)
        else:
            self.trains.append(train)

    def add_station(self, station):
        """
        Add one (or multiple) station(s) to the track.
        """
        if type(station) == list:
            for s in station:
                self.stations.append(s)
        else:
            self.stations.append(s)

    def available_platform(self, station):
        """
        Check if there is an platform available for the given station. 
        If so, return the platform. 
        Else return False, False value need to be handled where called.
        """
        for platform in station.platforms:
            if isinstance(platform.state, EmptyState):
                platform.state == OccupiedState()
                return platform
        
        return False

    def platform_on_event(self, station, platform_num, event):
        """
        Trigger an given event on the given station on platform with the given number.
        """
        platform = station.get_platform_by_num(platform_num)
        platform.state = platform.on_event(event)