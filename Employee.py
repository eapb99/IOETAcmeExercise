class Employee:

    def __init__(self, name, schedule):
        self.name = name
        self.schedule = schedule

    def __repr__(self):
        return f"{self.name}"

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.name == other.name and self.schedule == other.schedule
        return False
