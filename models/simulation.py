import datetime
import threading, time

class Simulation(object):
    """
    Main class. Keeps track of time and all ongoing events.
    """
    def __init__(self):
        self.tracks = []
        self.scheduled_trains = []
        self.current_time = datetime.datetime(2019,1,1,5)

    def print_info(self):
        """
        Print info of all tracks, stations, trains and platforms.
        """
        for number, track in enumerate(self.tracks):
            print(f"Track {number}:")
            print("    Stations:")
            for station in track.stations:
                print(f"        {station}:")
                [print(f"            {platform}") for platform in station.platforms]
            print("    Trains:")
            [print(f"        Train {train.num}: {train}") for train in track.trains]
    
    def add_track(self, track):
        """
        Add one (or multiple) track(s) to the simulation.
        """
        if type(track) == list:
            for t in track:
                self.tracks.append(t)
        else:
            self.tracks.append(track)
    
    def add_time(self, end, callback=None):
        """
        Goes one minute further in the future, a callback can be just to check for events
        """
        if end == 0:
            pass
        else:
            self.current_time += datetime.timedelta(minutes=1)
            print(self.current_time)
            time.sleep(1)
            callback()
            self.add_time(end-1, callback)

    def schedule_journey(self, journey):
        """
        Add one (or multiple) journey(s) to the simulation.
        """
        if type(journey) == list:
            for j in journey:
                self.scheduled_trains.append(j)
        else:
            self.scheduled_trains.append(journey)
        

    def check_journeys(self):
        """
        Check for every journey in the simulation if there should be an event trigger this minute.
        """
        current_min = self.current_time.minute
        for journey in self.scheduled_trains:
            if journey.departure_minute == current_min:
                journey.start()
                print(f"Train {journey.train.num} started it's journey from {journey.departure_station} to {journey.arrival_station}!")
            elif journey.arrival_minute == current_min:
                journey.stop()
                print(f"Train {journey.train.num} arrived at {journey.arrival_station} (Platform {journey.train.current_platform.platform_num}) from {journey.departure_station}!")
    
    def run(self, minutes):
        """
        Runs simulation by keeping track of time and following if trains should leave a station, or are approaching a station.
        """
        self.add_time(minutes, self.check_journeys)
