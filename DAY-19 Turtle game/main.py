person1 = input("enter person1 name: ")
person2 = input("enter person2 name: ")

combine = person1 + person2
lower = combine.lower()

t = lower.count('t')
r = lower.count('r')
u = lower.count('u')
e = lower.count('e')

first_digit = t+r+u+e

l = lower.count('l')
o = lower.count('o')
v = lower.count('v')
e = lower.count('e')

second_digit = l+o+v+e

print(first_digit)
print(second_digit)