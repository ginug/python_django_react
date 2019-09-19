#!/usr/bin/env
import airtravel as a
from pprint import pprint as pp
def main():
    fl=a.make_flight()
    #f1=A.make_fight()
    #fl=a.Aircraft('G-EUPT',  'Airbus A319', num_rows=22, num_seats_per_rows=4)
    print('The seating plan: {}'.format(fl.seating_plan()))

    f=a.Flight('SN1234', fl)
    print(f.number())
    pp( f._seating)
    f.allocate_seat("10B","Ginu")
    pp( f._seating) 
    f.allocate_seat("10C","Tintu")
    pp( f._seating) 

    f.reallocate_seats("Ginu","10B","01A")
    pp( f._seating) 
    pp(f.num_available_seats())
    
    
    a.booking_card_printer('Ginu','10A','ABCD','Boing')

if __name__=='__main__':
    main()



