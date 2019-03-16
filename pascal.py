# Pascal's Triangle
# In mathematics, Pascal's triangle is a triangular array of the binomial coefficients. 
# In much of the Western world, it is named after the French mathematician Blaise Pascal, 
# although other mathematicians studied it centuries before him in India,[1] Persia (Iran)[2], 
# China, Germany, and Italy.[3]

# The rows of Pascal's triangle are conventionally enumerated starting with row n = 0 at the 
# top (the 0th row). The entries in each row are numbered from the left beginning with k = 0 
# and are usually staggered relative to the numbers in the adjacent rows. The triangle may be 
# constructed in the following manner: In row 0 (the topmost row), there is a unique nonzero 
# entry 1. Each entry of each subsequent row is constructed by adding the number above and to 
# the left with the number above and to the right, treating blank entries as 0. For example, 
# the initial number in the first (or any other) row is 1 (the sum of 0 and 1), whereas the 
# numbers 1 and 3 in the third row are added to produce the number 4 in the fourth row.

# Source: Wikipedia, URL: https://en.wikipedia.org/wiki/Pascal%27s_triangle

def pascal(depth):
    res = [[1]]
    for i in range(0, depth):
        layer = [1]
        for j in range(0, len(res[i]) - 1):
            try:
                layer.append(res[i][j] + res[i][j + 1])
            except:
                layer.append(2)
        layer.append(1)
        res.append(layer)
    return res

pascal(10) # --> OUTPUT:
# [[1],
# [1, 1],
# [1, 2, 1],
# [1, 3, 3, 1],
# [1, 4, 6, 4, 1],
# [1, 5, 10, 10, 5, 1],
# [1, 6, 15, 20, 15, 6, 1],
# [1, 7, 21, 35, 35, 21, 7, 1],
# [1, 8, 28, 56, 70, 56, 28, 8, 1],
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
# [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]]