# class ab:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#     def hello(self):
#         self.h = "Hello"
# d = ab()
# d.hello()
# print(ab.__dict__)
# a = type("python",(),{'a' : 5,'b':"Hello World"})
# k = a()
# print(type(k))

# Python = type("python",(),{'a' : 5,'b':"Hello World"})
# k =Python()
# print(k.__dict__)
# print(Python.__dict__)

class myMeta(type):
    def __new__(cls, name, base,dict ):
        def speak(self):
            print("Hi")
        dict['speak'] = speak
        return super().__new__(cls,name,base,dict)
class A(metaclass=myMeta):
    pass
a = A()
a.speak()