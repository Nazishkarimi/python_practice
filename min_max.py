###############################################################################################################################
# Program to find smallest, largest number & their indices in a random list of given size. It also evaluates the mean/average #
###############################################################################################################################

import random
random_list = []

for i in range(1, 11):
    random_list.append(random.randint(100,1000))
print(random_list)
min_val = random_list[0]
min_ind = 0
max_val = random_list[0]
max_ind = 0
mean_val = random_list[0]

#to find minimum value & index
min_val = min(random_list)
min_ind = random_list.index(min_val)
'''
for i in range(1,len(random_list)):
    if min_val > random_list[i]:
        min_val = random_list[i]
        min_ind = i
'''
print('Minimum Value is: ',min_val)
print('Minimum Index is: ',min_ind)

#to find maximum value & index
max_val = max(random_list)
max_ind = random_list.index(max_val)
'''
for i in range(1,len(random_list)):
    if max_val < random_list[i]:
        max_val = random_list[i]
        max_ind = i
'''
print('Maximum Value is: ',max_val)
print('Maximum Index is: ',max_ind)

#to find mean value
mean_val = sum(random_list)/len(random_list)
'''
for i in range(1,len(random_list)):
    mean_val = mean_val + random_list[i]
'''
print('Mean value is: ',mean_val/len(random_list))
