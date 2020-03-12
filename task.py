a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
leagth = len(a)#длина списка

#1
'''
for x in a:
    if x<5:
        print (x)
'''
#2
'''
res = []
for elem in a:
    if elem in b:
        res.append(elem)
print (res)
'''
#3
'''
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
result = dict(sorted(d.items(), key=operator.itemgetter(1)))#убывание
result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))#Возрастание
print (result)
'''
#example
'''
fruits = ['lemon', 'pear', 'watermelon', 'tomato']
print("\n",fruits[0], fruits[1], fruits[2], fruits[3],"\n")
print(*fruits,"\n")
print(fruits)
'''




