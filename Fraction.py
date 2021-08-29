import math

def calculate_gcd(a, b):
    while b:
        a, b = b, a%b
    return a

class Fraction(object):
    def __init__(self, numerator, denominator = 1):
        self.numerator = numerator
        self.denominator = denominator
        self.reduction()

    def __str__(self):
        if self.denominator != 1:
            return "%s/%s" % (self.numerator, self.denominator)
        else:
            return "%s" % self.numerator

    def __add__(self, other):
        numerator = self.numerator * other.denominator \
                    + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        answer = Fraction(numerator, denominator)
        answer.reduction()
        return answer

    def __sub__(self, other):
        numerator = self.numerator * other.denominator \
                    - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        answer = Fraction(numerator, denominator)
        answer.reduction()
        return answer

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        answer = Fraction(numerator, denominator)
        answer.reduction()
        return answer

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = other.numerator * self.denominator
        answer = Fraction(numerator, denominator)
        answer.reduction()
        return answer

    def reduction(self):
        gcd = calculate_gcd(abs(self.numerator), abs(self.denominator))
        self.numerator //= gcd
        self.denominator //= gcd

    def getMixed(self):
        if self.denominator != 1:
            return "%s+%s/%s" % (self.numerator//self.denominator, self.numerator % self.denominator , self.denominator)
        else:
            return "%s" % self.numerator
