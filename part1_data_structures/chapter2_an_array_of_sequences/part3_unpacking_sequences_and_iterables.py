#  parallel assignment - assigning items from an iterable to a tuple of variables
lax_coordinates = (33.9425, -118.408056)
latitude, longitutde = lax_coordinates
latitude
longitutde

# swapping the values of variables without usinga temporary variable
b, a = a, b

# prefixing an argument with * when calling a function
divmod(20, 8)

t = (20, 8)
divmod(*t)

quotient, reminder = divmod(*t)
quotient, reminder

# the os.path.split() function builds a tuple (path, last_part)
# from a filesystem path
import os
_, filename = os.path.split('/home/colo/.ssh/file_name.txt')
filename

# Defining function parameters with *args to grab arbitrary excess arguments
a, b, *rest = range(5)
a, b, rest

a, b, *rest = range(3)
a, b, rest

a, b, *rest = range(2)
a, b, rest

# In the context of parallel assignment, the * prefix can be applied 
# to exactly one variable, but it can appear in any position
a, *body, c, d = range(5)
a, body, c, d

*head, b, c, d = range(5)
head, b, c, d

# In function calls, we can use * multiple times:
def fun(a, b, c, d, *rest):
    return a, b, c, d, rest

fun(*[1, 2], 3, *range(4, 7))

# The * can also be used when defining list, tuple, or set literals
*range(4), 4
[*range(4), 4]
{*range(4), 4, *(5, 6, 7)}

# The target of an unpacking can use nesting. 
# Each tuple holds a record with four fields, the last of which is a coordinate pair
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}') # unpack the coordinates
    for name, _, _, (lat, lon) in metro_areas:
        if lon <=0: # test selects only cities in the Western hemisphere
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

if __name__ == "__main__":
    main()