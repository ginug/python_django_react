"""
Create a class to model airtravel
"""

class Flight:
    def __init__(self, number):
        self._number=number
        if not self._number[:2].isalpha():
            raise ValueError("No airlaine code in '{}'".format(str(self._number)))
        if not self._number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".str.format(str(self._number)))
        if not self._number[2:].isdigit() and self._number <=9999 :
            raise ValueError("Invalid route number '{}'".str.format(str(self._number)))
    def number(self):
        return self._number
