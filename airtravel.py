"""
Create a class to model airtravel
Accepts an Aircraft number and an aircraft
"""

class Flight:
    def __init__(self, number, aircraft):
        self._number=number
        self._aircraft=aircraft
        if not self._number[:2].isalpha():
            raise ValueError("No airlaine code in '{}'".format(str(self._number)))
        if not self._number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".str.format(str(self._number)))
        if not self._number[2:].isdigit() and self._number <=9999 :
            raise ValueError("Invalid route number '{}'".str.format(str(self._number)))
    
    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft._model()


class Aircraft:
        def __init__(self,  registration, model, num_rows, num_seats_per_rows):
            self._registration = registration
            self._model = model
            self._num_rows = num_rows
            self._num_seats_per_rows = num_seats_per_rows
        
        def registration(self):
            return self._registration

        def model(self):
            return self._model
            
        def seating_plan(self):
           return ( range(1, self._num_rows + 1), "ABCDEFJK"[:self._num_seats_per_rows])