# In John's car the GPS records every s seconds the distance travelled from an origin(distances are measured in an arbitrary but consistent unit). For example, below is part of a record with s = 15:

# x = [0.0, 0.19, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25]
# The sections are:

# 0.0-0.19, 0.19-0.5, 0.5-0.75, 0.75-1.0, 1.0 - \
#     1.25, 1.25-1.50, 1.5-1.75, 1.75-2.0, 2.0-2.25
# We can calculate John's average hourly speed on every section and we get:

# [45.6, 74.4, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0]
# Given s and x the task is to return as an integer the * floor * of the maximum average speed per hour obtained on the sections of x. If x length is less than or equal to 1 return 0 since the car didn't move.

# Example:
# with the above data your function gps(s, x)should return 74

# Note
# With floats it can happen that results depends on the operations order. To calculate hourly speed you can use:

# (3600 * delta_distance) / s.

import unittest
from math import floor

import math
def gps(s, x):
    sections = [j - i for i, j in zip(x[::1], x[1::])]
    average_hour = [(3600*i)/s for i in sections]
    max_average = max(average_hour, default=0)
    return math.floor(max_average)

class Test(unittest.TestCase):

    def test_1(self):
        x = [0.0, 0.23, 0.46, 0.69, 0.92, 1.15, 1.38, 1.61]
        s = 20
        u = 41
        self.assertEqual(gps(s,x), u)

# x = [0.0, 0.11, 0.22, 0.33, 0.44, 0.65, 1.08, 1.26, 1.68, 1.89, 2.1, 2.31, 2.52, 3.25]
# s = 12
# u = 219
# testing(gps(s, x), u)
# x = [0.0, 0.18, 0.36, 0.54, 0.72, 1.05, 1.26, 1.47, 1.92, 2.16, 2.4, 2.64, 2.88, 3.12, 3.36, 3.6, 3.84]
# s = 20
# u = 80
# print(gps(s, x))
# x = [0.0, 0.01, 0.36, 0.6, 0.84, 1.05, 1.26, 1.47, 1.68, 1.89, 2.1, 2.31, 2.52, 2.73, 2.94, 3.15]
# s = 14
# u = 90
# print(gps(s, x))
# lista = list(zip(x[::1],x[1::]))
# print(lista )
# x = [0.0, 0.02, 0.36, 0.54, 0.72, 0.9, 1.08, 1.26, 1.44, 1.62, 1.8]
# s = 17
# u = 72
# testing(gps(s, x), u)
# x = [0.0, 0.24, 0.48, 0.72, 0.96, 1.2, 1.44, 1.68, 1.92, 2.16, 2.4]
# s = 12
# u = 72
# testing(gps(s, x), u)
# x = [0.0, 0.02, 0.44, 0.66, 0.88, 1.1, 1.32, 1.54, 1.76]
# s = 17
# u = 88
# testing(gps(s, x), u)
# x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.32, 1.54, 1.76, 1.98, 2.2, 2.42, 2.76, 2.99, 3.22, 3.45]
# s = 16
# u = 76
# testing(gps(s, x), u)
# x = [0.0, 0.01, 0.36, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75]
# s = 17
# u = 82
# testing(gps(s, x), u)
# x = [0.0, 0.2, 0.4, 0.69, 0.92, 1.15, 1.38, 1.61, 1.92, 2.16, 2.4, 2.64, 2.88, 3.12, 3.36]
# s = 19
# u = 58
# testing(gps(s, x), u)
# x = []
# s = 19
# u = 0
# testing(gps(s, x), u)
# x = [0.0]
# s = 19
# u = 0
# testing(gps(s, x), u)



if __name__ == '__main__':
    unittest.main()
