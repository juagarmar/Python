m = 10
list=[]
number = 0 

for k in range(m+1):
  for x in range(k-1):
    for i in range (x+1):
      list.append(i)
      number+=i

print(list)
print(' ')
print(f'The total sum of the numbers is {number}')
