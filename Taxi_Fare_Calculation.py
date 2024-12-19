def calculate_fare(distance):
    base_fare = 50
    distance_fare_rate = 10
    total_fare = base_fare + (distance * distance_fare_rate)
    return total_fare

def main():
    num_trips = int(input("Enter the number of trips: "))
    trips = []
    for i in range(num_trips):
        distance = float(input(f"Enter the distance for trip {i+1} in km: "))
        trips.append(distance)
    
    total_fare = 0
    for i in range(len(trips)):
        distance = trips[i]
        trip_fare = calculate_fare(distance)
        print("Trip", i + 1, ":", "$", trip_fare)
        total_fare += trip_fare
    
    print("Total Fare:", "$", total_fare)

main()
