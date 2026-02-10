def display():
    # ye ... if you use this with __docs__ it will print this inside!...
    # will work """ this also but documentation works only once. """
    '''This is a display fxn'''
    abcd="something"
    pass

def Sample(msg):
    print("Here is your msg: {}".format(msg))

#print(dir(display))
print(display.__doc__)
print(display.__dir__())
Sample("Yo, Sup")

print("""       21, Bakers Street
holla at me
""")

def test():
    return "23.33 text val"
print(test())

val=Sample("abcd")

print(val, type(val))
