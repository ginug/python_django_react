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
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]
        
    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft._model()

    def _parse_seat(self, seat):
       rows, seat_letters = self._aircraft.seating_plan() 
       row_text = seat[:2]
       letter= seat[-1]
       if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter) )
       try:
            row=int(row_text)
       except ValueError:
             raise ValueError("Invalid seat row {}".format(row_text))
        
       if row not in rows:
             raise ValueError("Invalid  row number {}".format(row_text))
        
       return row,letter

    def allocate_seat(self,seat, passenger):
        """
        Args - Seat eg 12A , Passenger eg - Beulah
        Seat assigned to passenger if valid (available, valid row, valid letter)
        """
        row,letter=self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} is already occupied".format(seat))

        self._seating[row][letter]=passenger

    def reallocate_seats(self, passenger, initial_seat, new_seat):
            row,letter = self._parse_seat(new_seat)
            self._seating[row][letter]=passenger
            initial_row , initial_letter=self._parse_seat(initial_seat)
            self._seating[initial_row][initial_letter]=None

    def num_available_seats(self):
        return sum(sum(1 for seat in row.values() if seat is None )
                    for row in self._seating if row is not None)
        
    def gen_passenger_seats(self):
         rows, seat_letters = self._aircraft.seating_plan()
         for row in rows:
              if row is not None:
                  for sl in seat_letters:
                      passenger=self._seating[row][sl]
                      if passenger is not None:
                          yield (passenger , "{}{}".format(row,sl))
      
    def print_card(self, gen_passenger_seats):
        for passenger,seat in  self.gen_passenger_seats():
            booking_card_printer(passenger, seat, self.number(), self.airline())
         
class Aircraft:
        def __init__(self,  registration):
            self._registration = registration
                   
        def registration(self):
            return self._registration
                   
        def num_seats(self):
           rows, row_seats = self.seating_plan()
           return len(rows) * len(row_seats)
        
class BOEING_Aircraft(Aircraft):
    
    def model(self):
        return 'BOEING'
    
    def seating_plan(self):
        return (range(1,23),"ABCD")
    
    
class AIRBUS_Aircraft(Aircraft):
    def model(self):
        return 'AIRBUS'
    
    def seating_plan(self):
        return (range(1,26),"ABCDEF")

def make_flight():
    return AIRBUS_Aircraft('G-EUPT')

def booking_card_printer(passenger, seat, flight, aircraft):
    """
    Create the format for the booking card and print it
    """
    output="|" \
           "   Name: {0}" \
           " Seat: {1}" \
           " Flight: {2}" \
           " Aircraft: {3}" \
            "        |".format(passenger, seat, flight, aircraft)
    upper_line=' '+'_'*(len(output)-2)
    lower_line=' '+'_'*(len(output)-2)
    empty_line1='|'+' '*(len(output)-2) +'|'    
    empty_line2='|'+'_'*(len(output)-2)+'|' 
    lines=[upper_line, empty_line1, output, empty_line2,]
    card= '\n'.join(lines)
    print(card)
    print()
    
     