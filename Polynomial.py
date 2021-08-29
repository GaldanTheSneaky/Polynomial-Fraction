import numpy as np
from itertools import zip_longest

def normalize(poly):
    while poly and poly[-1] == 0:
        poly.pop()
    if poly == []:
        poly.append(0)


class Polynomial:

    def __init__(self, *coefficients):
        self.coefficients = list(coefficients)

    def __call__(self, x):
        res = 0
        for coeff in self.coefficients:
            res = res * x + coeff
        return res

    def degree(self):
        return len(self.coefficients)

    def __add__(self, other):
        c1 = self.coefficients[::-1]
        c2 = other.coefficients[::-1]
        res = [sum(t) for t in zip_longest(c1, c2, fillvalue=0)]
        res.reverse()
        return Polynomial(*res)

    def __sub__(self, other):
        c1 = self.coefficients[::-1]
        c2 = other.coefficients[::-1]
        res = [t1 - t2 for t1, t2 in zip_longest(c1, c2, fillvalue=0)]
        res.reverse()
        return Polynomial(*res)

    def __mul__(self, other):
        new_pol_list = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for o1, i1 in enumerate(self.coefficients):
            for o2, i2 in enumerate(other.coefficients):
                new_pol_list[o1 + o2] += i1 * i2

        new_pol = Polynomial(*new_pol_list)
        return new_pol

    def __truediv__(self, other):
        num = self.coefficients
        normalize(num)
        den = other.coefficients
        normalize(den)

        if len(num) >= len(den):
            shiftlen = len(num) - len(den)
            den = [0] * shiftlen + den
        else:
            return [0], num

        quot = []
        divisor = float(den[-1])
        for i in range(shiftlen + 1):
            mult = num[-1] / divisor
            quot = [mult] + quot

            if mult != 0:
                d = [mult * u for u in den]
                num = [u - v for u, v in zip(num, d)]

            num.pop()
            den.pop(0)

        normalize(num)
        new_pol = Polynomial(*quot)
        new_pol_remainder = Polynomial(*num)
        return new_pol, new_pol_remainder

    def __floordiv__(self, other):
        num = self.coefficients
        normalize(num)
        den = other.coefficients
        normalize(den)

        if len(num) >= len(den):
            shiftlen = len(num) - len(den)
            den = [0] * shiftlen + den
        else:
            return [0], num

        quot = []
        divisor = float(den[-1])
        for i in range(shiftlen + 1):
            mult = num[-1] / divisor
            quot = [mult] + quot

            if mult != 0:
                d = [mult * u for u in den]
                num = [u - v for u, v in zip(num, d)]

            num.pop()
            den.pop(0)

        new_pol = Polynomial(*quot)
        return new_pol

    def __mod__(self, other):
        num = self.coefficients
        normalize(num)
        den = other.coefficients
        normalize(den)

        if len(num) >= len(den):
            shiftlen = len(num) - len(den)
            den = [0] * shiftlen + den
        else:
            return [0], num

        quot = []
        divisor = float(den[-1])
        for i in range(shiftlen + 1):
            mult = num[-1] / divisor
            quot = [mult] + quot

            if mult != 0:
                d = [mult * u for u in den]
                num = [u - v for u, v in zip(num, d)]

            num.pop()
            den.pop(0)

        normalize(num)
        new_pol_remainder = Polynomial(*num)
        return  new_pol_remainder


    def cut_off(self):
        counter = 0
        for coefficient in self.coefficients:
            if coefficient == 0:
                counter += 1
            else:
                break

        for i in range(counter):
            self.coefficients.remove(0)

    def __repr__(self):
        return "Polynomial" + str(self.coefficients)

    def __str__(self):

        def x_expr(degree):
            if degree == 0:
                res = ""
            elif degree == 1:
                res = "x"
            else:
                res = "x^" + str(degree)
            return res

        degree = len(self.coefficients) - 1
        res = ""

        for i in range(0, degree + 1):
            coeff = self.coefficients[i]
            if abs(coeff) == 1 and i < degree:
                res += f"{'+' if coeff > 0 else '-'}{x_expr(degree - i)}"
            elif coeff != 0:
                res += f"{coeff:+g}{x_expr(degree - i)}"

        return res.lstrip('+')

    def __abs__(self):
        return self

    def __bool__(self):
        if len(self.coefficients) == 1 and self.coefficients[0] == 0:
            return False
        else:
            return True