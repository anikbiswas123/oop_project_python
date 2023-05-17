from Employee import employee


class hourlyEmployee(employee):
    def __init__(self, first_name, last_name, working_hours, rate):
        super().__init__(first_name, last_name)
        self.working_hours = working_hours
        self.rate = rate

    def get_salary(self):
        return self.working_hours * self.rate
