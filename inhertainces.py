# class employee:
#     def __init__(self, name, base_pay):
#         self.name = name
#         self.base_pay = base_pay
#
#     def get_pay(self):
#         return self.base_pay
#
#
# class salesEmployee(employee):
#
#     def __init__(self, name, base_pay, sales_in):
#         self.name = name
#         self.base_pay = base_pay
#         self.sales_in = sales_in
#
#     def get_pay(self):
#         return self.base_pay + self.sales_in
#
#
# employee = employee("sumilon", 12000)
# print(employee.get_pay())
# sale = salesEmployee("Jhon", 12000, 500)
# print(sale.get_pay())


# class person:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#
#     def get_full_name(self):
#         return  self.fname + " "+self.lname
#
#
# class employee(person):
#     def __init__(self ,fname,lname,salry,other):
#         super().__init__(fname,lname)
#         self.salary=salry
#         self.other=other
#
#     def get_salar(self):
#         return self.salary
#
#
# emp=employee("sumilon","biswas",12000,3000)
# print(emp.get_full_name())
# print(emp.fname)
# print(emp.lname)
#
# print(emp.get_salar())



class employee:
    def __init__(self,name,base_pay):
        self.name=name
        self.base_pay=base_pay

    def get_pay(self):
        return self.base_pay

    def display(self):
        return self.name


class salesEmployee(employee):
    def __init__(self,name,base_pay,sales_in):
        super().__init__(name,base_pay)
        self.sales_in=sales_in

    def get_pay(self):
        return  super().get_pay()+self.sales_in



s=salesEmployee("Roni",12000,6000)
print(s.get_pay())
print(s.display())

