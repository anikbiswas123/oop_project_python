# class person:
#     def __init__(self, firstname, lastname, age):
#         # data hiding or encapsation of data private
#         self.__fname = firstname
#         self.__lastname = lastname
#         self.__age = age
#
#     ## getter setter user korta paran
#     def set_fname(self, fname):
#         self.__fname = fname
#
#     def get_fname(self):
#         return str(self.__fname)
#
#
#     def set_age(self, age):
#         if age >= 18:
#             self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#
#
#     def get_full_info(self):
#         return self.__fname + " " + self.__lastname + " " + str(self.__age)
#
#
# person = person("John", "Doie", 32)
#
# print(person.get_full_info())
# print(person.get_fname())
# person.set_fname("sumilon")
# print(person.get_fname())
# person.set_age(20)
# print(person.get_age())


# class circle:
#     def __init__(self, r):
#         self.pi = 3.1416
#         self.r = r #redius
#
#     def area(self):
#         return self.pi * self.r ** 2
#
#     def circle_ferences(self):
#         return 2 * self.pi * self.r
#
#
# c=circle(10)
# print(c.area())
# print(c.circle_ferences())


# defining the defualt value

# class product:
#     defualt_dicount = 0
#
#     def __init__(self, price):
#         self.price = price
#         self.discount = product.defualt_dicount
#
#     def set_discount(self, discount):
#         self.discount = discount
#
#     def net_prices(self):
#         return self.price - ((self.price * self.discount) / 100)
#
#
# p = product(200)
# # print(p.net_prices())
#
# p.set_discount(10)
# print(p.net_prices())

#
# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def __eq__(self, other):
#         return self.first_name == other.first_name





#
#
# john = Person('John', 'Doe', 25)
# jane = Person('John', 'Doe', 227)
# print(john == jane)  # True


class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


my_list = MyList("Rahamin")
print(len(my_list))  # Output: 5
