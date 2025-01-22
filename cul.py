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
        - test (int): Counter for iterations (unused).
        - der (list[float]): Coefficients of the derivative.
        - fx (float): Value of the polynomial at `x1`.
        - fx_pr (float): Value of the derivative at `x1`.
        - new_x (float): Updated value of the root estimate.
        """
        valid = 1e-10
        max = 100
        test = 0
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

        # Ensure _x1 < _x2 for consistency
        if _x1 == _x2:
            return "The x values must be different"
        elif _x1 > _x2:
            x1 = _x2
            x2 = _x1
        else:
            x1 = _x1
            x2 = _x2

        # Attempt to find roots using different methods
        z1 = self.brute(x1, x2)  # Brute-force search for a root
        z2 = self.newton(x1)     # Newton's method starting from x1
        z3 = self.newton(x2)     # Newton's method starting from x2
        deg = self.__Poly.get_order()  # Degree of the polynomial
        roots = []  # List to store found roots

        # If no roots are found using any method, return message
        if z1 is None and z2 is None and z3 is None:
            return "No roots between given values"
        # checking if linear
        elif deg < 2: 
            if z1 is not None: #if there is a root return it
                return z1
            else:
                return "No roots between given x values"
        # If Newton's method converges to the same root for both bounds, return that root
        elif round(z2, 9) == round(z3, 9): 
            if x1-0.1 < z2 < x2+0.1 and x1-0.1 < z3 < x2+0.1:
                return z2
        # For polynomials of degree less than 3, return z2 and z3 directly
        elif deg == 2: # for quadratic
            if x1-0.1 < z2 < x2+0.1 and x1-0.1 < z3 < x2+0.1: # check if the 2 roots are within the range
                return z2, z3
            elif x1-0.1 < z2 < x2+0.1: # check first root individually
                return z2
            elif x1-0.1 < z3 < x2+0.1: # check second root individually
                return z3
            else: # if both fail then no root is between the x-values
                return "no root given between x values"
                
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
                if x2 < c or c < x1: # if a root not within the range provided is found ignore it
                    pass
                else:
                    zeroes.append(c) # otherwise append it to zeroes
            if zeroes == []:
                return "No roots in given x range" # if there are no zeroes let the user know
            return zeroes # otherwise return zeroes
