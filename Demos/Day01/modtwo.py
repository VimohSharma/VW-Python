import modone
print("modetwo is {} ".format(__name__))

__y__="something" 

def add(x,y):
    return x+y

print(add(3,4))

modone.task2()
# in this currect namescape scope how many functinalities are here, wont show other modules in other modules, it is decided in runtime
#print(dir())