# P50: Based on Mosteller's 50 Challenging Problems in Probability

These are numeric solutions when it was too complicated or long winded to solve the problem by hand.

## Problem 1b: Probability of choosing two pairs of socks both red is 1/2 and an even number of black pairs

### Command
```
→ python3 p1b.py
```

### Solution
```
...
r + b = N: 15 + 6 = 21, P = 1 / 2.0
```

## Problem 7: Curing the gambler
Probability that gambler will be behind after 36 rolls in about 3/4
```
>>> 2*(37/38)**35*(36.5/38)
0.7553943362209891
```