person = {'name': 'Jenn', 'age': 23}
sentence = f"My name is {person['name']} and I am {person['age']} years old"
print(sentence)

calculation = f'4 times eleven is equal to {11*4}'
print (calculation)

for n in range(1,11):
  sentence = f'The value is {n:04}'
  print (sentence)

pi = 3.14159265
sentence = f'Pi is equal to {pi:.4f}'
print (sentence)

from datetime import datetime

birthday = datetime(1990,1,1)
sentence = f'Jenn has a birthday on {birthday:%B %d, %Y}'
print (sentence)
