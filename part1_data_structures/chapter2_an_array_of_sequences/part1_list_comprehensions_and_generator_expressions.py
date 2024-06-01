import array

# Example 2-1. Build a list of Unicode code points from a string
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

codes

# Example 2-2. Build a list of Unicode code points from a string, using a listcomp
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
codes

# “Walrus operator” := remain accessible after those comprehensions or 
# expressions return—unlike local variables in a function
x = 'ABC'
codes = [ord(x) for x in x]
# x was not clobbered: it’s still bound to 'ABC'
x
codes

codes = [last := ord(c) for c in x]
# last remains
last
# c is gone; it existed only inside the listcomp.
#c


# Listcomps Versus map and filter
# Example 2-3. The same list built by a listcomp and a map/filter composition
# The filter and map built-ins can be composed to do the same,
# but readability suffers
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
beyond_ascii

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
beyond_ascii


# Cartesian Products
# Example 2-4. Cartesian product using a list comprehension
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
# This generates a list of tuples arranged by color, then size
tshirts = [(color, size) for color in colors for size in sizes]
tshirts

# Note how the resulting list is arranged as if the for loops were 
# nested in the same order as they appear in the listcomp.
for color in colors:
    for size in sizes:
        print(color, size)
# To get items arranged by size, then color, just rearrange the for clauses; 
# adding a line break to the listcomp makes it easier to see how the result 
# will be ordered.
tshirts = [(color, size) for size in sizes for color in colors]
tshirts


# Generator Expressions
# Example 2-5. Initializing a tuple and an array from a generator expression
symbols = '$¢£¥€¤'
# If the generator expression is the single argument in a function call, 
# there is no need to duplicate the enclosing parentheses.
tuple(ord(symbol) for symbol in symbols)

#The array constructor takes two arguments, so the parentheses around the 
# generator expression are mandatory. The first argument of the array 
# constructor defines the storage type used for the numbers in the array.
array.array('I', (ord(symbol) for symbol in symbols))

# Example 2-6. Cartesian product in a generator expression
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)