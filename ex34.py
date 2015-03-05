# Accessing Elements of Lists

def the_animal_at(i):
    animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
    ordinal = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
    return "The %s animal is at %d and is a %s.\n    The animal at %d is the %s animal and is a %s.\n" % (ordinal[i], i, animals[i], i, ordinal[i], animals[i])

def the_nth_animal(i):
    i -= 1
    animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
    ordinal = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
    return "The %s animal is at %d and is a %s.\n    The animal at %d is the %s animal and is a %s.\n" % (ordinal[i], i, animals[i], i, ordinal[i], animals[i])

print "1. ", the_animal_at(1)
print "2. ", the_nth_animal(3)
print "3. ", the_nth_animal(1)
print "4. ", the_animal_at(3)
print "5. ", the_nth_animal(5)
print "6. ", the_animal_at(2)
print "7. ", the_nth_animal(6)
print "8. ", the_animal_at(4)

# Study Drills
# 1. With what you know of the difference between these types of numbers, can
# you explain why the year 2010 in "January 1, 2010," really is 2010 and not 
# 2009? (Hint: you can't pick years at random.)

# Since you can't pick years at random, they are ordinal numbers and start at 
# 1 instead of 0. The first year was marked 1 and 2009 years later, it's 2010.

# 2. Write some more lists and work out similar indexes until you can 
# translate them.



# 3. Use Python to check your answers.