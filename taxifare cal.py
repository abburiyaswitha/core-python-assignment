def calculate_fare(distance):
    base_fare = 50
    distance_fare = 10
    return base_fare + (distance * distance_fare)
trips = []
num_trips = int(input("Enter the number of trips:"))
for i in range(num_trips):
    distance = float(input(f"Enter the distance for trip {i+1} in km:"))
    trips.append(distance)
total_fare = 0
for i, distance in enumerate(trips, start=1):
    fare = calculate_fare(distance)
    print(f"Trip {i}: ${fare}")
    total_fare += fare
print(f"\nTotal Fare: ${total_fare}")
