# Example 2-9. Method from an imaginary Robot class
# match/case handling sequences

def handle_command(self, message):
    match message: # Python will try to match "message" to the patterns in each case clause
        case ['BEEPER', frequency, times]: # this pattern matches any subject with three items. 
            self.beep(times, frequency)    # The first item must be a 'BEEPER', the second and third item can be anything, and will be bound to variables times and frequency.
        case ['NECK', angle]: # this pattern matches to subject with two items, the firs being 'NECK'
            self.rotate_neck(angle)
        case ['LED', ident, intensity]: # this one will match to the subject with 3 items and starting with LED
            self.leds[ident].set_brightness(ident, intensity) # If the items does not match, Python proceeds to the next case.
        case ['LED', ident, red, green, blue]:
            self.leds[ident].set_color(ident, red, green, blue)
        case _: # this is the default case. It will match any subject that did not match a previous pattern.
            raise InvalidCommand(message)


# As a first example of destructuring, Example 2-10 shows part of Example 2-8 rewritten with match/case
# Example 2-10. Destructuring nested tuples—requires Python ≥ 3.10
metro_areas = [
('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for record in metro_areas:
        match record:
            case [name, _, _, (lat, lon)] if lon <= 0:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

# A sequence pattern matches the subject if:
# - the subject is a sequence and
# - the subject and the pattern have the same number of items and
# - each corresponding item matches, including nested items

main()

# You can bind any part of a pattern with a variable using the 'as' keyword:
"""case [name, _, _, (lat, lon) as coord]"""

# Here the first item has to be an instance of string and two last items in the 2-tuple must be instances of float
"""case [str(name), _, _, (float(lat), float(lon))]"""

# Here it matches any subject suquence starting with string, and ending with nested sequence of two floats
"""case [str(name), *_, (float(lat), float(lon))]"""


