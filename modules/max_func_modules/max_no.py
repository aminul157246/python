import utils
print(utils.find_max([3,4,6]))   # 6

# or 

from utils import find_max
print(find_max([5,6,8]))   # 8

# but this is also possible using max method 
arr = [9,5,7]
print(max(arr))