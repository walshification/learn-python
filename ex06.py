# Initializes variable x with a string being interpolated with a formatter.
x = "There are %d types of people." % 10
# Initializes a variable called "binary" with the value "binary".
binary = "binary"
# Initializes a variable called "do_not" with the value "don't".
do_not = "don't"
# Initializes variable y with a string and two formatters assigned to the 
# values of the above variables.
y = "Those who understand %s and those who %s." % (binary, do_not)

# Prints variable x.
print x
# Prints variable y.
print y

# Prints the string with the x variable interpolated inside it.
print "I said: %r." % x
# Prints the string with the y variable interpolated inside it.
print "I also said: '%s'." % y

# Initializes variable hilarious with the boolean value False.
hilarious = False
# Initializes variable joke_evaluation with the value of a string and empty 
# formatter.
joke_evaluation = "Isn't that joke so funny?! %r"

# Prints the joke_evaluation statement with the hilarious variable as the 
# value of the formatter within it.
print joke_evaluation % hilarious

# Initializes variable w with a string value.
w = "This is the left side of..."
# Initializes variable e with a string value.
e = "a string with a right side."

# Prints strings w and e concatenated together with +.
print w + e
