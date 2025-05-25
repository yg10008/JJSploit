class Car:
    def __init__(self, make, year, model, api_data):
        self.make = make
        self.year = year
        self.model = model
        self.api_data = api_data

    def to_dict(self):
        return {
            "make":  self.make,
            "year":  self.year,
            "model": self.model,
            "api_data": self.api_data
        }
