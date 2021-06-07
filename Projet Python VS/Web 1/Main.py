from Dog import Dog
from Car import Car

tuture = Car(200,10,4)
voiture = Car(-500,0,-5)

tuture.add_person_in_car("Loic")
tuture.add_person_in_car("Paul")
tuture.add_person_in_car("Alice")
tuture.add_person_in_car("Germaine")
tuture.add_person_in_car("Bob")

tuture.del_person_in_car("Loic")

for person in tuture.person_in_car:
    print(person)

tuture.move(100,5)

print("distance",tuture.distance)
print("Fuel",tuture.current_fuel)
print("Speed",tuture.current_speed)