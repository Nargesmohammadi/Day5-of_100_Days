eng2sp = {}
eng2sp['one'] = 'undo'
eng2sp['two'] = 'dos'
print(eng2sp)

eng2sp2 = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp2)
print(eng2sp2['two'])
print(eng2sp['one'])

inventory = {'apples': 340, 'bananas': 451, 'oranges': 512}
print(inventory)

del inventory['apples']
print(inventory)
print(len(inventory))
print(eng2sp2.keys())
print(eng2sp2.values())
print(eng2sp2.items())

# print(eng2sp2.has_key('one'))

opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
print(opposites)
alias = opposites
copy = opposites.copy()
copy['right'] = 'left'
print(opposites['right'])
alias['right'] = 'left'
print(opposites['right'])
copy['right'] = 'privilege'
print(opposites['right'])

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(range(1, 10, 2))

numbers = [17, 123]
print(numbers[0])
print(numbers[3 - 2])
print(numbers[-1])
print(numbers[-2])
# print(numbers[-3]): list index out of range

fruits = ['apple', 'orange', 'banana', 'peach']
i = 0
while i < 4:
    print(fruits[i])
    i = i + 1

fruits1 = ['apple', 'orange', 'banana', 'peach']
i = 0
while i < len(fruits1):
    print(fruits1[i])
    i = i + 1

list1 = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
i = 0
while i < len(list1):
    print(list1[i])
    # print(len(list1[i]))
    print(type(list1[i]))
    if type(list1[i]) in (list, tuple, dict, str):
        print(len(list1[i]))
    else:
        print("not a list")
    i = i + 1

if 'spam' in fruits:
    print(1)
else:
    print(0)

for i in list1:
    print(i)

for fruit in fruits:
    word = str(fruits)
    print("I like to eat" + word + "s!")

a = [1, 2, 3]
b = [4, 5, 6, 7]
c = a + b
print(c)

var = [0] * 3
print(var)

list2 = ['a', 'b', 'c', 'd', 'e', 'f']
var1 = list2[1:3]
print(var1)
var2 = list2[:4]
print(var2)
var3 = list2[3:]
print(var3)
var4 = list2[1:4]
print(var4)
list2[1:3] = ['x', 'y']
print(list2)

del list2[1]
print(list2)

n = "asma"
m = "asma"
print(id(n))
print(id(m))
print(id(list1))
print(id(list2))

list3 = list2
list3[4] = 'g'
print(list3)

a = ['s', 'd', 'h', 't']
b = a[:]
print(b)
b[0] = 'l'
print(a)
print(b)
