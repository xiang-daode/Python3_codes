import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)                   # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a            # does not create a reference
print(d['primary'] )               # fetch the object if it is still alive

del a                       # remove the one reference
print(gc.collect() )               # run garbage collection right away
print(d['primary'] )               # entry was automatically removed
