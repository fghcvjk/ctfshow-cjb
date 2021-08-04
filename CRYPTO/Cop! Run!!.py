from Crypto.Util.number import *
from flag import flag

n = 1 << 8
p = getPrime(n)
print(p)

P.<t> = PolynomialRing(Zmod(p))
f = t * t + randrange(p)
print(f)

x = [randrange(p)]
x += [f(x[0])]
print([x_ >> (n - ceil(5 * n / 7)) for x_ in x])

flag = bytes_to_long(flag)
y = f(x[-1])
for i in range(7):
    y = f(y)
    flag ^^= int(y)
print(flag)

'''
92946459607669937513774102250057295249718593723232674702212854287358873135783
t^2 + 43844336985235863734419631630425915388298791521868754583032904718644333115590
[3248642833056635029095920782095626337949113592116495266, 4883935221919623989344404485025479346028101682781790392]
193207529097125793778662519051231322609402866155819915933598367395102313904490702547833
'''