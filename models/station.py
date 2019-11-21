class Station(object):
    """ 
    class Station keep track of its Platforms.
    """

    def __init__(self, station_name, previous_station=None, next_station=None):
        """ Initialize the Station. """

        # Start with a default state.
        self.station_name = station_name
        self.platforms = []

    def add_platform(self, platform):   
        """
        Add one (or multiple) platform(s) to the station.
        """
        if type(platform) == list:
            for p in platform:
                self.platforms.append(p)
        else:
           self.platforms.append(platform)

    def get_platform_by_num(self, num):
        """
        Retrieve Platform object based on given number.
        """
        for platform in self.platforms:
            if platform.platform_num == num:
                return platform
        return False
    
    def __str__(self):
        return f"Station {self.station_name}"

    def __repr__(self):
        return self.__str__()