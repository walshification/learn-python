# This imports the argv feature from the sys module.
from sys import argv

# This defines the arguments from the command line.
script, filename = argv

# This sets and opens the file assigning it to the txt variable.
txt = open(filename)

# Prints the line with the name of the file interpolated into it.
print "Here's the file %r:" % filename
# This prints out the file on the command line.
print txt.read()
