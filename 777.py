import inspect
import sys
# import turtle
#
# print(inspect.ismodule(turtle))
# print(inspect.isclass(turtle))
# print(inspect.isfunction(turtle))
#
# print(inspect.getmodule(turtle.back))
# print(inspect.getmodule(list))

#class Human:
#    def __init__(self, age, height, name = "John"):
#        self.age = age
#        self.height = height
#        self.name = name

#sig = inspect.signature(Human)
#print(sig)
#for param in sig.parameters.values():
#    print(param.name, param.default)

# print(sys.executable)
# print(sys.version)
# print(sys.argv)
#
# for module_name , module_path in sys.modules.items():
#     print(module_name, module_path)

for _ in dir(__builtins__):
    print(_)

