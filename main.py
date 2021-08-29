from Fraction import Fraction
from Polynomial import Polynomial


pol = Polynomial(2, 2)
pol1 = Polynomial(3, 2)
pol2 = Polynomial(-4, 5)
pol3 = Polynomial(-7, 2)


fract = Fraction(pol, pol1)
fract1 = Fraction(pol2, pol3)


print(pol)
print(pol2)

pol4 = (pol + pol2)
pol5 = pol1 + pol3
fract3 = Fraction(pol4, pol5)
print(fract + fract1)
print(fract3)