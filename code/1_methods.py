# lambda, map, filter, reduce, copy, Shallow copy, Deep copy


# lambda
ld_test = lambda x, y, z: x*y+z
print(ld_test(1, 2, 3))

# map
target = [1, 2, 3, 4, 5]
map_test = list(map(lambda k: k+30, target))
print(map_test)

# filter
f_target = list(range(1, 100))
f_test = list(filter(lambda x: x% 3 == 0, f_target))
print(f_test)

# reduce
from functools import reduce
r_target = list(range(1, 10))
r_test = reduce(lambda x, y:x+y, r_target)
print(r_test)

# Copy
co_a = [1, 2, 3, 4]
co_b = co_a # 같은 주소값
co_b[1] = 71
print('co_a=', co_a)
print('co_b=', co_b)


# Shallow Copy
import copy
sc_a = [1, 2, 3, [100, 200]]
sc_b = copy.copy(sc_a) # sc_a 안에 list가 있을 경우 같은 주소값
sc_b[0] = 1004
sc_b[3][0] = 1005
print('sc_a=', sc_a)
print('sc_b=', sc_b)


# Deep Copy
dc_a = [4, 5, 6, [101, 201]]
dc_b = copy.deepcopy(dc_a) # sc_a 안에 list가 있을 경우 같은 주소값
dc_b[0] = 40
dc_b[3][0] = 1010
print('dc_a=', dc_a)
print('dc_b=', dc_b)

