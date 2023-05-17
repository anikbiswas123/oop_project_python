# class Product:
#     default_discount = 0
#
#     def __init__(self, price):
#         self.price = price
#         self.discount = Product.default_discount
#
#     def set_discount(self, discount):
#         self.discount = discount
#
#     def net_price(self):
#         return self.price * (1 - self.discount)
#
#
# p1 = Product(100)
# print(p1.net_price())
#
# class Product:
#     default_discount = 0
#
#     def __init__(self, price):
#         self.price = price
#         self.discount = Product.default_discount
#
#     def set_discount(self, discount):
#         self.discount = discount
#
#     def net_price(self):
#         return self.price * (1 - self.discount)
#
#
# p1 = Product(100)
# print(p1.net_price())
#  # 100
#
# print("set the defualt discount")
#
# p2 = Product(200)
# p2.set_discount(0.05)
# print(p2.net_price())
#  # 190


# class Person:
#     def __init__(self, first_name, last_name,age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     def __repr__(self):
#         return f'Person("{self.first_name}","{self.last_name}",{self.age})'
#
#     def __str__(self):
#         return f'person("{self.first_name}","{self.last_name}","{self.age}")'
#
#
# person=Person("John","Doe",24)
# print(person)
# print("==================")
# print(repr(person))


class person:
    price = 0

    def __init__(self, fname, lnaame, age, education):
        self.fname = fname
        self.lname = lnaame
        self.age = age
        self.education = education

    def full_name(self):
        return str(self.fname + " " + self.lname)  # method

    def p_info(self):
        return (self.fname + " " + self.lname + " " + str(self.age))

    def person_ed(self):
        return str(self.fname + " " + self.lname + " " + self.education)


person = person()
person.price = 9000
print(person.price)


#
# print(person.person_ed())
# print(person.full_name())
# print(person.p_info())

class Person1:
    pass


print(Person1)
