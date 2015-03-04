people = 30
cars = 40
trucks = 15


# The if checks whether it is True that cars outnumber people.
if cars > people:
    # If the above line resolves to True, this code is executed.
    print "We should take the cars."
# If line 7 is False, this line checks if people outnumber cars.
elif cars < people:
    # If the above line resolves to True, this code is executed.
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
