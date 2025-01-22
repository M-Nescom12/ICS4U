import math

class Polynomial:
    def __init__(self, func):
        """
        Pre-conditions: 
        - `func` is a list of coefficients representing a polynomial, ordered from the highest to lowest degree.

        Post-conditions:
        - Initializes the polynomial object with encapsulated coefficients, length, and an empty equation string.

        Variable Dictionary:
        - func (list[int/float]): Input list of polynomial coefficients.
        - self.__func (list[int/float]): Encapsulated version of `func` for internal use.
        - self.__len (int): Length of the `func` list.
        - self.__eq (str): Empty string to hold the polynomial's string representation.
        """
        self.__func = func
        self.__len = len(func)
        self.__eq = ""
   
    def craft(self):
        """
        Pre-conditions:
        - `self.__func` contains the coefficients of the polynomial.

        Post-conditions:
        - Constructs and returns a string representation of the polynomial.

        Variable Dictionary:
        - i (int): Index of the current coefficient in the iteration.
        - c (int/float): Current coefficient being processed.
        - piece (str): Part of the equation string representing a term of the polynomial.
        """
        i = 0  # Initialize the term index.
        for c in self.__func:
            # Handle the sign for coefficients.
            if i == 0 and c < 0:
                c = -c
                self.__eq += "-" # accounting for a negative value at the beginning
            
            # Choosing correct sign (+/-)
            elif 0 < i < self.__len and c > 0 and self.__eq != "":
                self.__eq += " + "
            elif 0 < i < self.__len and c < 0 and self.__eq != "":
                self.__eq += " - "
                c = -c
                 
            # Skip terms with zero coefficient.
            if c == 0:
                pass
                
            elif c == 1:
                # Handle coefficients of 1 for different positions.
                if self.__len - 1 == i:
                    self.__eq += str(c)
                elif self.__len - 2 == i:
                    self.__eq += 'x' # add 'x'
                else:
                    piece = "x^" + str(self.__len - i - 1) # add x^ (degree)
                    self.__eq += piece
            else:
                # Handle coefficients other than 1.
                if self.__len - 1 == i:
                    self.__eq += str(c)
                elif self.__len - 2 == i:
                    piece = str(c) + 'x' # add value + 'x'
                    self.__eq += piece
                else:
                    piece = str(c) + "x^" + str(self.__len - i - 1) # add value + x^ (degree)
                    self.__eq += piece
           
            i += 1  # Move to the next term.
        return self.__eq  # Return the constructed equation string.
   
    def get_order(self):
        """
        Pre-conditions:
        - `self.__func` contains the coefficients of the polynomial.

        Post-conditions:
        - Returns the highest degree of the polynomial, or -1 if all coefficients are zero.

        Variable Dictionary:
        - i (int): Index of the current coefficient in the iteration.
        """
        i = 0  # Initialize the index.
        while i < self.__len:
            if self.__func[i] != 0:  # Find the first non-zero coefficient.
                return self.__len - i - 1  # Return its degree.
            i += 1  # Move to the next coefficient.
        return -1  # Return -1 if no non-zero coefficients are found.
   
    def f(self, x: float):
        """
        Pre-conditions:
        - `x` is a float or int value representing the input to the polynomial.
        - `self.__func` contains the coefficients of the polynomial.

        Post-conditions:
        - Returns the result of evaluating the polynomial at `x`.

        Variable Dictionary:
        - i (int): Index of the current coefficient in the iteration.
        - y (float): Accumulated result of the polynomial evaluation.
        - x (float): The input value where the polynomial is being evaluated.
        """
        i = 0  # Initialize the term index.
        y = 0.0  # Initialize the result.
        for c in self.__func:
            # Add each term's contribution to the result.
            if i == self.__len - 1:
                y += c
            elif i == self.__len - 2:
                y += x * c
            else:
                y += x ** (self.__len - (i + 1)) * c
            i += 1  # Move to the next term.
        return y  # Return the evaluated result.
           
    def __str__(self):
        """
        Pre-conditions:
        - The polynomial equation string (`self.__eq`) has already been constructed.

        Post-conditions:
        - Returns the string representation of the polynomial.

        Variable Dictionary:
        - self.__eq (str): String representation of the polynomial.
        """
        return f"{self.__eq}"
