'''
A=5.0
B=0
C=A+B
F="0"
D="Hello World!!"*80000#Выведет 80000 раз
'''
'''
print (F)
'''
'''
del A #Удаляет переменую
name = input("\nКак вас вас зовут? ").lower()#Ввод
print ("Првет,",name)#Выведет
'''
'''
num_1 = int(input("Num_1: "))#Цифра
num_2 = int(input("Num_2: "))#Цифра
res = num_1 + num_2#Сложит цифры
print ("Result is", res)#Выведет цифру

str_1 = input("Something")#По умолчанию присваивает строку
str_2 = input("Something")
res = str_1 + str_2#Склеит cтроки
print ("Result is", res)#Выведет цифру
'''
'''
if name == "степан":#Условие
    print ("Пошел отсюда\n")#После вывода пренесет строчку
elif name == "маша" or name == "мария" or  name == "mока" or name == "mariya" or name == "mokushka" or name == "masha":#or-или
    Masha = input("А к вам еще обращаются? ").lower()
    if Masha == "маша" or Masha == "мария" or  Masha == "mока"  or Masha == "mariya" or Masha == "mokushka" or Masha == "masha":
        print ("Рад встречи")
    else:
        print ("Самозванец")
else:
    print ("OK")#Выведет на новой строчке
'''
'''
i=int(2)
p="Start"
while i>10:#пока i>10 будетвыполняться условие
    print (p)
    i/=2
    p=int(i)

for j in 'hello world':#Берем каждое значение после in
    if j == 'z':
        break
        #break - прерывает
        #continue - пропускает
    #print(j*2, end = '')#Выводим кадое значение после in, end - строка которуюследует поставить после объекта
else:#работает с break
    print ('w')
'''

l=[]#пустой список
lis = [1,56,'x',34,2.34, ['S','t','r','o','k','a']]#Список

a=[a+b for a in 'list' if a != 's' for b in 'soup' if b != 'u']#Создаем список в котором склеиваем буквы слова 'list' и 'soup', при этом пропускаем 's' в слове 'list' и 'u' в слове 'soup'
print(*a)