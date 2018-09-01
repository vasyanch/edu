import math
import this_module 


l = [2]
l += [x ** 2 for x in (2 ,3, 4, 5)]

k_for = []
for i in l:
    k_for.append(math.sqrt(i))

print('k_for =>', k_for)



k_map = list(map(math.sqrt, l))
print('k_map =>', k_map)


k_gen_list = [math.sqrt(i) for i in l]
print('k_gen_list =>', k_gen_list)



