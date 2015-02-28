# Initializes a variable named "cars" and assigns it a value of 100.
cars = 100
# Initializes a variable named "space_in_a_car" and assigns it a value of 4.0,
# which is a floating point number.
space_in_a_car = 4.0
# Initializes a variable named "drivers" and assigns it a value of 30.
drivers = 30
# Initializes a variable named "passengers" and assigns it a value of 90.
passengers = 90
# Initializes a variable named "cars_not_driven" and assigns it a value of
# the number of cars minus the number of drivers.
cars_not_driven = cars - drivers
# Initializes a variable named "cars_driven" and assigns it the value of 
# drivers.
cars_driven = drivers
# Initializes a variable named "carpool_capacity" and assigns it a value 
# by multiplying the cars_driven by space_in_a_car.
carpool_capacity = cars_driven * space_in_a_car
# Initializes a variable named "average_passengers_per_car" and assigns it 
# a value by dividing the passengers by cars_driven.
average_passengers_per_car = passengers / cars_driven


# Prints the statement using the above variable.
print "There are", cars, "cars available."
# Prints the statement using the above variable.
print "There are only", drivers, "drivers available."
# Prints the statement using the above variable.
print "There will be", cars_not_driven, "empty cars today."
# Prints the statement using the above variable.
print "We can transport", carpool_capacity, "people today."
# Prints the statement using the above variable.
print "We have", passengers, "to carpool today."
# Prints the statement using the above variable.
print "We need to put about", average_passengers_per_car, "in each car."
