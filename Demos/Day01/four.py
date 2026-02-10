data = [10,20,30,40,50,60] # Iterable: collection

#Iteration: loop
#Iterator: object

# for ele in data:
print(dir(data))

x = data.__iter__()
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())


iter_obj = iter(data)
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

iter_object = iter(data)
for item in iter_object:
    print(item)

# previous index will remember only takes one memory, saves memory, and prints next better than for loop

def my_for_loop(iterable):
    iterator = iter(iterable)
    try:
        while True:
            print(next(iterator))
    except StopIteration:
        pass

my_for_loop(data)


