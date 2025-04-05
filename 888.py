# print (f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}")
#
# try:
#     print("start")
#     print(10/0)
#     print("no error")
# except NameError:
#     print("У вас помилка NameError")
# except ZeroDivisionError:
#     print("У вас помилка ZeroDivisionError")

# try:
#     print("start")
#     print(10/0)
#     print("no error")
# except (NameError, ZeroDivisionError) as error:
#     print(f"У вас помилка {error}")

# try:
#     try:
#         print("start")
#         print(error)
#         print("no error")
#     except SyntaxError:
#         print("Wrong Syntax")
# except NameError as error:
#     print(error)

# try:
#     print("hello")
# except:
#     print("we have error")
# else:
#     print("No problems")
# finally:
#     print("Final Code")

# def checker(var1):
#     if type(var1) = str:
#         raise TypeError(f"Вибачте, функція не працює {type(var1)}, нам потрібен рядок(str)")
#     else:
#         return var1
#
# first_var = 123
# checker(first_var)

# class BuildingError(Exception):
#     def __str__(self):
#         return f"With so much material the house cannot be built!"
# def check_material(ammount, limit):
#     if amount > limit:
#         return 'enought material'
#     else:
#         raise BuildingError(amount)
# materials = 123
# check_material((materials, 300))

import warnings

warnoings.simplefilter("ignore", SyntaxWarning)
warnoings.simplefilter("always", ImportWarning)
warnings.warn("Warning, no code here", SyntaxWarning)

try:
   warning.warn("Warning, module not import", ImportWarnig)
except:
    print("Warning processed")