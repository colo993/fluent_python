# Example 2-7. Tuples used as records
# Sorting the tuple would destroy the information because the meaning of each
# field is given by its position in the tuple.
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), 
                ('ESP', 'XDA205856')]
# As we iterate over the list, passport is bound to each tuple
# The % formatting operator understands tuples and treats each item 
# as a separate field
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

# The for loop knows how to retrieve the items of a tuple separately—this 
# is called “unpacking.” Here we are not interested in the second item, so we 
# assign it to _, a dummy variable.
for country, _ in traveler_ids:
    print(country)


# Be aware that the immutability of a tuple only applies to the references
# contained in it. References in a tuple cannot be deleted or replaced. But if 
# one of those references points to a mutable object, and that object is 
# changed, then the value of the tuple changes
a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])
a == b
b[-1].append(99)
a == b

# If you want to determine explicitly if a tuple (or any object) has a fixed 
# value, you can use the hash built-in to create a fixed function like this:
def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True

tf = (10, 'alpha', (1, 2))
tm = (10, 'alpha', [1, 2])
fixed(tf)
fixed(tm)