zones_to_cross = int(input("How many zones must I cross? "))
print(zones_to_cross)
print("Crossing zones...")
# reverse counts from users provided integer printing each iteration.
for zone in range(zones_to_cross, 0, -1):
    print("...crossed zone", zone)
print("Crossed all zones.  Jumanji!")