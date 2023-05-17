#
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
#
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self,new_age):
#         self.__age=new_age
#
#     age=property(fget=get_age)
#
#
#
#
# pp=person("sumilon",79)
#
#
# print(pp.get_age())
# print("propertic")
#
# pp.set_age(30)
# print(pp.age)

# import math
#
#
# class Circle:
#     def __init__(self, radius):
#         self._radius = radius
#         self._area = None
#
#     @property
#     def radius(self):
#         return self._radius
#
#     @radius.setter
#     def radius(self, value):
#         if value < 0:
#             raise ValueError('Radius must be positive')
#
#         if value != self._radius:
#             self._radius = value
#             self._area = None
#
#     @property
#     def area(self):
#         if self._area is None:
#             self._area = math.pi * self.radius ** 2
#
#         return self._area
#
# c=Circle(10)
# # print(c.area)
#
# c.radius = 14
# print(c.area)

#
# class person:
#     def __init__(self, p_name, age):
#         self.__p_name = p_name
#         self.__age = age
#
#     def get_name(self):
#         return self.__p_name
#
#     def set_name(self, value):
#         self.__p_name = value
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, value):
#         self.__age = value
#
#     def del_name(self):
#         del self.__p_name
#
#     #
#     # age = property(fget=get_age, fset=set_age)
#     # name=property(fget=get_name,fset=set_name,fdel=del_name)
#
#
#
# p = person("sumilon", 23)
# print(p.age)
# print(p.name)
#
# p.age = 15
# p.name="sukhaina"
# print(p.age)
# print(p.name)
# del p.name
# print(p.name)

from pprint import pprint


class Person:
    def __init__(self, name):
        self._name = name


    def get_name(self):
        return self._name


    def set_name(self, value):
        if value.strip() == '':
            raise ValueError('name cannot be empty')
        self._name = value


    def del_name(self):
        del self._name
    name=property(fget=get_name,fset=set_name,fdel=del_name)

p=Person("sumilon")
print(p.name)
p.name = "Rasel"
del p.name
print(p.name)

