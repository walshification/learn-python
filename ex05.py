name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
ht_in_cm = height * 2.54
wt_in_kg = weight * 0.453592

print "Let's talk about %s." % name
print "He's %d inches tall. That's %d in centimeters." % (height, ht_in_cm)
print "He's %d pounds heavy. That's %d in kilograms." % (weight, wt_in_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(
    age, height, weight, age + height + weight)