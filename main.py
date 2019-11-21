import sys
sys.path.append('models')
from track import Track
from train import Train
from station import Station
from trackplatform import Platform
from simulation import Simulation
from journey import Journey

# Create main track
track_1 = Track()
track_2 = Track()

# Create stations, add platforms, and create connections
station_1 = Station("Amersfoort")
station_1.add_platform(Platform(1))

station_2 = Station("Den Dolder")
station_2.add_platform(Platform(1))
station_2.add_platform(Platform(2))

station_3 = Station("Bilthoven")
station_3.add_platform(Platform(1))

# Add stations to track
track_1.add_station([station_1, station_2])
track_2.add_station([station_3, station_2])

# Add train and place on station 1
train_1 = Train(1, track_1, station_1)
train_2 = Train(2, track_2, station_3)

# Add train to track
track_1.add_train(train_1)
track_2.add_train(train_2)

# Create Simulation object which handles time and checks journeys for all tracks
sim = Simulation()
sim.add_track([track_1, track_2])

train_1_journey_1_forward = Journey(train_1, station_1, station_2, 6, 12)
train_1_journey_2_forward = Journey(train_1, station_1, station_2, 36, 42)
train_1_journey_1_back = Journey(train_1, station_2, station_1, 15, 21)
train_1_journey_2_back = Journey(train_1, station_2, station_1, 45, 51)

sim.schedule_journey([train_1_journey_1_forward, train_1_journey_2_forward, train_1_journey_1_back, train_1_journey_2_back])

train_2_journey_1_forward = Journey(train_2, station_3, station_2, 8, 13)
train_2_journey_2_forward = Journey(train_2, station_3, station_2, 38, 43)
train_2_journey_1_back = Journey(train_2, station_2, station_3, 16, 21)
train_2_journey_2_back = Journey(train_2, station_2, station_3, 46, 51)

sim.schedule_journey([train_2_journey_1_forward, train_2_journey_2_forward, train_2_journey_1_back, train_2_journey_2_back])

sim.print_info()
sim.run(100) # Run 100 minutes of simulation
sim.print_info()
