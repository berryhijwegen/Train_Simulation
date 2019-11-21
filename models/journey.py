class Journey(object):
    """
    Small class to schedule a train ride.
    """
    def __init__(self, train, dep_st, arr_st, dep_min, arr_min):
        self.train = train
        self.departure_station = dep_st
        self.arrival_station = arr_st
        self.departure_minute = dep_min
        self.arrival_minute = arr_min

    def start(self):
        """
        Start the ride. (On departure)
        """
        self.train.on_event('starting', self.arrival_station)
    
    def stop(self):
        """
        Stop the ride. (On arrival)
        """
        self.train.on_event('stopping', self.arrival_station)