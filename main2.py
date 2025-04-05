# intro_list = []
#
# for method in dir(into_list):
#     print(method)

# data = "text"
#
# print(hasattr(data, "replace"))
# print(hasattr(data, "reverse"))
# print(getattr(data, "startswith"))
# print(getattr(data, "startswith", None))
# print(getattr(data, "reverse", None))
#
# def first_func():
#     pass
#
# print(callable(data))
# print(callable(first_func))

class First:
    pass

class Second(First):
    pass

print(issubclass(First, Second))
print(issubclass(Second, First))

obj = Second()

print(isinstance(obj, Second))
print(isinstance(obj, First))
