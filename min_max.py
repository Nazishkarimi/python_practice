import random
random_list = []

for i in range(1, 101):
    random_list.append(random.randint(100,1000))
print(random_list)
min_val = random_list[0]
min_ind = 0
max_val = random_list[0]
max_ind = 0
mean_val = random_list[0]

#to find minimum value & index
for i in range(1,len(random_list)):
    if min_val > random_list[i]:
        min_val = random_list[i]
        min_ind = i
print('Minimum Value is: ',min_val)
print('Minimum Index is: ',min_ind)

#to find maximum value & index
for i in range(1,len(random_list)):
    if max_val < random_list[i]:
        max_val = random_list[i]
        max_ind = i
print('Maximum Value is: ',max_val)
print('Maximum Index is: ',max_ind)

#to find mean value
for i in range(1,len(random_list)):
    mean_val = mean_val + random_list[i]
print('Mean value is: ',mean_val/len(random_list))
