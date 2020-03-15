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
    #print(j*2, end = '')#Выводим кадое значение после in, end - строка которую следует поставить после объекта
else:#работает с break
    print ('w')
'''
'''
l=[]#пустой список
lis = [1,56,'x',34,2.34, ['S','t','r','o','k','a']]#Список

a=[a+b for a in 'list' if a != 's' for b in 'soup' if b != 'u']#Создаем список в котором склеиваем буквы слова 'list' и 'soup', при этом пропускаем 's' в слове 'list' и 'u' в слове 'soup'

#print(l)

l.append (23)#Добавляет в конец списка
l.append (34)
l.extend (a)#Расширяет список списком "a"
l.insert (1, "Аллибаба")#Заменяет по индексу
l.append (23)
l.remove (23)#Удаляет элемент(первый встреченый)
l.pop ()#Удаляет по индексу и возварщает его(Если ничего не указано удаляет последний)
f = l.index (34)#Возвращает индекс элемента
g = l.count (34)#Сколько таких элементов есть в списке
#l.sort ()#Сотировка списка в порядке возврстания
l.reverse ()#Переворачивает список
l.clear ()#Очищает список

#print (g)
#print (f)
#print(l.pop (0))#Выведет удаленный  элемент
print(l)
'''
'''
q = [34,45,56,11]
#print(q[0])#Выводит по индексу
#print(q[-1])#Выводит последний по индексу

i = 0
while i < len(q):#Работает пока `i` меньше длины списка
    print (q[i], end = ' ')#Выводит элемент по индексу равный `i`,end - строка которую следует поставить после объекта
    i+= 1#Заменяет значение `i` значением на единицу больше

#item-Список [START-начало отсчета(по умолчанию равен 0):STOP-Длина списка:STEP-Шаг по умолчанию равен 1] - Срез
print ("\n",q[::2])
'''
'''
#Кортежи - нельзя менять
#a = (53,35,65.56,"ret")#Кортеж
#a = "Nothing", 67, 34 #Тоже Кортеж
#b = [53,35,65.56,"ret"]#Список

#print(a.__sizeof__())#Узнаем размер объекта. Кортеж весит меньше списка
#print(b.__sizeof__())

a = tuple ("Hello World")#Разделяет на отдельные элементы
print (a.count("H"))#Функции такие же как у списка кроме изменения
'''
'''
#d = {"test": 1, "test_2" : "TesT"}#Словарь - у каждого элемента есть ключ по которому мы обращаемся к этому ключу 
#print (d["test"])
#d = dict(short="dict", longer='dictionary')
#print (d)
#d = dict([(23,34),(56,87)])
#print (d)
#d = dict.fromkeys (["a","b"])#Создание только ключей
#d = dict.fromkeys (["a","b"],1)#Создание ключей и присваение к ним `1`
#d = {a : a**2 for a in range(7)}#В пределах 7(от 0 до 6) будет изменяться ключ `a` на единицу больше и элемент ключ в степени 2
#print (d)
person = {"name" : {"last_name": "Smith", "firt_name": "Jon", "middle_name": "Ivanovich"}, "address": ["г.Ижевск", "ул.Баранова","д.45","кв.45"],"phone":{"home_phone" : "34-45-56", "mobile_phone": "8-848-434-45-65", "moebile_phone_2": "Not"}}
print(person["name"]["last_name"])
'''
