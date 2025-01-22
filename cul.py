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
import math
from Polynomial import *

class IVT:
    def __init__(self, func):
        """
        Pre-conditions:
        - `func` is a list of coefficients representing a polynomial, ordered from the highest to lowest degree.

        Post-conditions:
        - Initializes the IVT object with the polynomial function, its length, and a Polynomial object.

        Variable Dictionary:
        - func (list[float]): Coefficients of the polynomial.
        - self.__func (list[float]): Encapsulated version of `func`.
        - self.__len (int): Length of the function (number of coefficients).
        - self.__Poly (Polynomial): Polynomial object to leverage existing methods.
        """
        self.__func = func
        self.__len = len(func)
        self.__Poly = Polynomial(func)
       
    def solve(self, x: float, y: float):
        """
        Pre-conditions:
        - `x` is a float representing the input to the polynomial.
        - `y` is a float to compare the polynomial evaluation against.

        Post-conditions:
        - Returns the difference between the polynomial evaluated at `x` and `y`.

        Variable Dictionary:
        - i (int): Index for iterating over coefficients.
        - exp (int): Exponent of the current term.
        - val (float): Accumulated value of the polynomial evaluation.
        """
        i = 0
        val = 0.0

        # Solving the function with both y and x
        while i < self.__len:
            exp = self.__len - i - 1
            val += self.__func[i] * (x ** exp)
            i += 1
        return val - y
   
    def derivative(self):
        """
        Pre-conditions:
        - None (uses `self.__func`).

        Post-conditions:
        - Returns a list of coefficients representing the derivative of the polynomial.

        Variable Dictionary:
        - derive (list[float]): Coefficients of the derivative.
        - i (int): Index for iterating over coefficients.
        - exp (int): Exponent of the current term.
        """
        derive = []
        i = 0
        # Takes the derivative of the polynomial and stores it in an array and retunrs it 
        while i < self.__len:
            exp = self.__len - i - 1
            if exp > 0 and self.__func[i] != 0:
                derive.append(self.__func[i] * exp)
            i += 1
        return derive
   
    def derive(self, der, x: float):
        """
        Pre-conditions:
        - `der` is a list of derivative coefficients.
        - `x` is the point at which the derivative is evaluated.

        Post-conditions:
        - Returns the derivative evaluated at `x`.

        Variable Dictionary:
        - val (float): Accumulated value of the derivative evaluation.
        - i (int): Index for iterating over `der`.
        - exp (int): Exponent of the current term.
        """
        val = 0.0
        # Solving F(x) (Derivative)
        for i in range(len(der)):
            exp = len(der) - i - 1
            val += der[i] * (x ** exp)
        return val
   
    def newton(self, x1: float):
        """
        Pre-conditions:
        - `x1` is the initial guess for the root.

        Post-conditions:
        - Returns the root found using Newton's method, or None if it fails.

        Variable Dictionary:
        - valid (float): Threshold for convergence.
        - max (int): Maximum iterations.
        - der (list[float]): Coefficients of the derivative.
        - fx (float): Value of the polynomial at `x1`.
        - fx_pr (float): Value of the derivative at `x1`.
        - new_x (float): Updated value of the root estimate.
        """
        valid = 1e-10
        max = 100
        der = self.derivative()
       
        # Doing Newton's method in a loop for 100 iterations
        for __ in range(max):
            fx = self.solve(x1, 0) # solving f(x)
            fx_pr = self.derive(der, x1) # Solving F(x1)

            if fx_pr == 0:  # Failsafe for division by zero.
                return None
           
            if __ == max - 1:  # Did not converge.
                return None
           
            new_x = x1 - fx / fx_pr # Determining new x based on y or y'
            if abs(new_x - x1) < valid:  # Convergence check.
                return new_x
            x1 = new_x # Setting x1 to new_x
        return None

    def brute(self, x1: float, x2: float):
        """
        Pre-conditions:
        - `x1` and `x2` define the interval within which a root is sought.

        Post-conditions:
        - Returns the root found using the bisection method, or None if no root exists.

        Variable Dictionary:
        - valid (float): Threshold for convergence.
        - f_x1 (float): Value of the polynomial at `x1`.
        - f_x2 (float): Value of the polynomial at `x2`.
        - avg (float): Midpoint of the current interval.
        - f_z (float): Value of the polynomial at `avg`.
        """
        
        valid = 1e-5   
        f_x1 = self.__Poly.f(x1) 
        f_x2 = self.__Poly.f(x2)
        
        if f_x1 * f_x2 > 0:
            return None  # No root if f(x1) and f(x2) have the same sign.

        # Loop to determine when f(x) = 0 using IVT
        while abs(x2 - x1) > valid: 
            avg = (x1 + x2) / 2 
            f_z = self.__Poly.f(avg) 

            # If root found that is sufficient for tolerence, return it
            if abs(f_z) < valid:
                return avg
            # Check if zero is closer to x1 so x2 will change to x average
            elif f_x1 * f_z < 0:  
                x2 = avg
                f_x2 = f_z
            # The zero is closer to x2 so x1 will change to x average
            else:  
                x1 = avg
                f_x1 = f_z

        return None

    def findZero(self, _x1: float, _x2: float):
        """
        Pre-conditions:
        - _x1 and _x2 must be floating-point numbers.
        - _x1 and _x2 must not be equal.
        
        Post-conditions:
        - Returns the roots of the polynomial within the range [_x1, _x2], if any exist.
        - Returns a sorted list of unique roots if multiple roots exist.
        - Returns a message if no roots exist in the given range.
        """

        # Variable Dictionary:
        # _x1, _x2: float - The bounds within which to search for roots.
        # x1, x2: float - Adjusted bounds ensuring x1 < x2.
        # z1: float or None - Root found using the brute-force method.
        # z2, z3: float or None - Roots found using Newton's method at bounds x1 and x2.
        # deg: int - Degree of the polynomial.
        # roots: list - List of unique roots found within the range.

        # Making x1 < x2 for simplicity
        if _x1 == _x2:
            return "The x values must be different"
        elif _x1 > _x2:
            x1 = _x2
            x2 = _x1
        else:
            x1 = _x1
            x2 = _x2
   
        deg = self.__Poly.get_order()  # Degree of the polynomial
        roots = []  # List to store found roots

        if deg == -1: # check if there is function
            return "No function given"
        
        # If a horizontal line that doesnt touch y = 0
        elif deg == 0:
            return "No zero found"
        
        elif deg == 1: # check if linear
            der = self.derivative()
            if der != 0:
                r =(0 - self.__func[self.__len-  1])/der[0] # solve for root
            # If zero is not in given x value range
            if x1 - 0.1 < r < x2 + 0.1:
                return f"The zero is: x = {r}"
            else:
                return "No zero between given x value range"
            
        # check if quadratic
        elif deg == 2:
            a = self.__func[self.__len - 3]
            b = self.__func[self.__len - 2]
            c = self.__func[self.__len - 1]
           
            QF = b**2 - (4 * a * c) # solve discriminant

            if QF > 0: # if discriminant is greater than 0
                # Solving for both roots
                r1 = ((-1 * b + (math.sqrt(QF)))/(2 * a))
                r2 = ((-1 * b - (math.sqrt(QF)))/(2 * a))
                
                # Returning only if in given x value range
                if x1 - 0.1 < r1 < x2 + 0.1 and x1 - 0.1 < r2 < x2 + 0.1:
                    return f"The zeroes are: x = {r1} and x = {r2}"
                elif x1 - 0.1 < r1 < x2 + 0.1:
                    return f"The zero is: x = {r1}" 
                elif x1 - 0.1 < r2 < x2 + 0.1:
                    return f"The zero is: x = {r2}"
                else: 
                    return "No zero between given x value range"
                
            elif QF == 0: # if discriminant is equal to 0
                # solvng for vertex
                r = (-1 * b)/(2 * a)
                if r == 0:
                    r = abs(r)
                # Returning only if in given range
                if x1 - 0.1 < r < x2 + 0.1:
                    return f"The zero is: x = {r}"
                else:
                    return "No zero in given x value range"
                
            else: # otherwise there are no roots
                return "No zero found..."
        
        # Attempt to find roots using different methods
        z1 = self.brute(x1, x2)  # Brute-force (IVT) search for a root
        z2 = self.newton(x1)     # Newton's method starting from x1
        z3 = self.newton(x2)     # Newton's method starting from x2
        
        # If no roots are found using any method, return message
        if z1 is None and z2 is None and z3 is None:
            return "No zero between given x value range"
        
        # If Newton's method converges to the same root for both bounds, return that root
        elif round(z2, 9) == round(z3, 9):
            # if newton missed a root
            pk = self.brute(x1, (z2-0.1))
            if pk is not None and pk != z2:
                if x1 - 0.1 < z2 < x2 + 0.1 and x1 - 0.1 < z3 < x2 + 0.1:
                    return f"x = {z1} and x = {z2}"
                
            elif x1 - 0.1 < z2 < x2 + 0.1 and x1 - 0.1 < z3 < x2 + 0.1:
                return f"x = {z2}"
            else:
                return "No zero between given x value range"
       
        # For higher-degree polynomials, find and return all unique roots
        else:
            roots.append(z2)  # Root closest to negative infinity
            roots.append(z3)  # Root closest to positive infinity

            i = 0
            while i < deg - 2:  # Continue finding additional roots
                # Using a ratio specific to the polynomial type.
                # Ex. if the order is 4, the most roots is 4 so the ratio would be set accordingly
                low = 1 / (deg - 1) 
                high = 1 - low
                z = self.newton((z2 * high + z3 * low))  # Test a point closer to z2 using test ratio

                # Check if the found root z is already in roots
                f = 0
                for r in roots:
                    if z is None or r is None: # if a root isn't found then pass
                        pass
                    elif round(r, 5) == round(z, 5): # otherwise check if the root has already been found
                        f = 1

                # Add z if it is a new root
                if f != 1 and z is not None: # if a new zero is found append it
                    roots.append(z)
                    z2 = z

                else:
                    # Try different combinations to find a new root
                    z = self.newton((z2 * 0.7 + z3 * 0.3))  # Test a point between already found zeroes closer to z2
                    f = 0
                    for r in roots:
                        if z is None or r is None: # if a root isn't found then pass
                            pass
                        elif round(r, 5) == round(z, 5): # otherwise check if the root has already been found
                            f = 1

                    if f != 1 and z is not None: # if a new zero is found append it
                        roots.append(z) 
                        z2 = z
                    else:
                        z = self.newton((z2 + z3) / 2)  # Midpoint of z2 and z3
                        f = 0
                        for r in roots:
                            if z is None or r is None: # if a root isn't found then pass
                                pass
                            elif round(r, 5) == round(z, 5): # otherwise check if the root has already been found
                                f = 1

                        if f != 1 and z is not None: # if a new zero is found append it
                            roots.append(z)
                            z2 = z
                        else:
                            # As a last resort, use brute-force to find a root in a small interval
                            # Will fail if there are even number of roots in between 
                            z = self.brute((z2 + 1e-4), (z3 - 1e-4))
                            if z is not None:
                                roots.append(z)
                                z2 = z
                i += 1
    
            roots.sort()  # Sort the roots for consistency
            zeroes = []
            for c in roots:
                if x2 < c or c < x1: # if a root is not within the range provided ignore it
                    pass
                else:
                    zeroes.append(c) # otherwise append it to zeroes
            if zeroes == []:
                return "No zeroes in given x range" # if there are no zeroes let the user know
            return f"The zeroes are:\nx = " + "\nx = ".join(map(str, zeroes))# returning zeroes
from Polynomial import *
"""
Author : Muntasir N
   Revison date : January 22, 2025
   Program : ICS4U0-1
   Description : A code that displays a polynomial equation and solves a polynomial function given an x-value

 General Variable Dictionary:
 - function (list[str]) the coefficients of the function
 - arr (list[str]) the filtered out version of the coefficients of the function
 - temp (list[str]) a list of coefficients each as their own term
 - func (list[int/float]) the final version of our list of coefficients as a float/int
 - x (float) an inputed x-value which the function will be solved for
"""

func = []
usr = (1, -21, 175, -735, 1624, -1764, 720, 0)
usr = str(usr)

# Uncomment the 2 lines below if you want to have input in the shell
#usr = input("Enter all coeffecients wihtout proceeding 0s: ")
#usr = str(usr)

# Cleans up input from user if using that feature, otherwise putting coeffecints in array
digits = usr.strip("()[]{}+")
floaty = digits.split(',')

# Converting type: str in the rray to type: float
for c in floaty:
    try:
        func.append(float(c))
    except ValueError:
        print("Please enter NUMBERS seperated by commas...") # For bad input
        exit()

# Retunring the equation
myPoly = Polynomial(func)
myPoly.craft()
print(myPoly)
        
x = input("Please input an x value you would like to solve the function for: ") # take input for an x-value the user would like the function to be solved for.
try:
    x = float(x) # make it a float
except ValueError:
    print("please input a proper number") # if a value error occurs output the issue to let the user know and exit the code
    exit()
    
# Solving f(x)
print(myPoly.f(x))
from IVT import *
from Polynomial import *

"""
Author : Muntasir Nathalia
   Revison date : January 22, 2025
   Program : ICS4U0-1
   Description : Code that finds the roots of a polynomial function
   
 General Variable Dictionary:
 - function (list[str]) the coefficients of the function
 - arr (list[str]) coefficients of the function stored array
 - temp (list[str]) a list of coefficients each as their own term
 - func (list[int/float]) the final version of our list of coefficients as a float/int
 - x1 - (float) the first point the roots of the function can be found within
 - x1 - (float) the second point the roots of the function can be found within
"""

func = []
usr = (-2,5,-3,0)
usr = str(usr)

# These are the functions I used [1, -21, 175, -735, 1624, -1764, 720, 0] or [1,-10,35,-50,24]
# Other test functions [-2,5,-3,0] or [1,-10,35,-50,24,,0]
# an input option has been made in case you want to easily put in your own coefficients just comment out the bit of code below
#usr = input("Enter all coeffecients seperated by commas: ")
#usr = str(usr)

# Cleans up input from user if using that feature, otherwise putting coeffecints in array
digits = usr.strip("()[]{}+")
floaty = digits.split(',')

# Converting type: str in the rray to type: float
for c in floaty:
    try:
        func.append(float(c))
    except ValueError:
        print(c)
        print("Please enter NUMBERS seperated by commas...") # For incorrect input
        exit()

# Calls Polynomial Object to output th equation
Poly = Polynomial(func)
Poly.craft()
print(Poly)

# Taking user input for a range to find the zeroes of the polynomial function
x1 = input("Please input a point before the root in the function: ")
x2 = input("Please input a point after the root in the function: ")
try:
    x1 = float(x1)
    x2 = float(x2)
except ValueError:
    print("Enter a value for x1, and x2")
    exit()

# Finds all zeroes in given range
Zero = IVT(func)
print(Zero.findZero(x1, x2))

