import sys
sys.path.append('models')
from track import Track
from train import Train
from station import Station
from trackplatform import Platform

# Create main track
track = Track()

# Create stations, add platforms, and create connections
station1 = Station("Yeet1") 
station1.add_platform(Platform(1))

station2 = Station("Yeet2")
station2.add_platform(Platform(1))

station1.set_next_station(station2)

station2.set_previous_station(station1)

# Add stations to track
track.add_station([station1,station2])

# Add train and place on station 1
train1 = Train(track,station1)

# Add train to track
track.add_train(train1)

print(f"(Train 1) {train1}")
train1.on_event('starting', station2)
print(f"(Train 1) {train1}")
train1.on_event('stopping')
print(f"(Train 1) {train1}")
print(f"(Station 2) {station2.get_platform_by_num(1)}")
train1.on_event('starting', station1)
print(f"(Train 1) {train1}")
train1.on_event('stopping')
print(f"(Train 1) {train1}")
print(f"(Station 2) {station2.get_platform_by_num(1)}")
print(f"(Station 1) {station1.get_platform_by_num(1)}")