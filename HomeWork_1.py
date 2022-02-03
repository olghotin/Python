# 1)Создать переменную типа String
# Тип str представляет строки.
# Строка представляет последовательность символов, заключенную в одинарные или двойные кавычки.
perem_str = 'Olga'

# 2)Создать переменную типа Integer
# Тип int представляет целое число.
perem_int = 34

# 3)Создать переменную типа Float.
# Тип float представляет число с плавающей точкой.
# В качесте разделителя целой и дробной частей используется точка.
perem_float = 16.01

# 4)Создать переменную типа Bytes
# Тип данных bytes - это неизменяемые последовательности отдельных байтов.
perem_bytes = bytes(123)

# 5)Создать переменную типа List
# List - представляет тип данных, который хранит набор или последовательность элементов.
# Для создания списка в квадратных скобках ([]) через запятую перечисляются все его элементы.
perem_list = [123, 456, 789, 'Python']

# 6)Создать переменную типа Tuple
# Tuple - это те же списки за одним исключением. Кортежи неизменяемые структуры данных.
# Так же как списки они могут состоять из элементов разных типов, перечисленных через запятую.
# Кортежи заключаются в круглые скобки.
perem_tuple = ('hello, world !',)
perem_tuple_2 = tuple('hello, world !')

# 7)Создать переменную типа Set.
# Set (множество)- это изменяемый неупорядоченный тип данных.
# В множестве всегда содержатся только уникальные элементы, которые разделены между собой запятой и заключены в фигурные скобки.
perem_set = {'Mom', 'Tue', 'Wed', 'Tue', 'Fri', 'Sat', 'Sun'}

# 8)Создать переменную типа Frozenset.
# Frozenset - это неизменяемое множество.
perem_frozenset_0 = frozenset('Hello')
perem_frozenset_1 = frozenset(['Olga', 'Alex', 'Bohdan'])

# 9)Создать переменную типа Dict.
# Dict представляет собой структуру данных, предназначенную для хранения произвольных объектов с доступом по ключу.
# Данные в словаре хранятся в формате ключ – значение.
perem_dict = {'key_1': 'Olga', 'key_2': 34, 'key_3': 'Kontush'}

#10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print('1) Perem_string =', perem_str)
print('Type =', type(perem_str))

print('*******************************')

print('2) Perem_integer =', perem_int)
print('Type =', type(perem_int))

print('*******************************')

print('3) Perem_float =', perem_float)
print('Type =', type(perem_float))

print('*******************************')

print('4) Perem_bytes =', perem_bytes)
print('Type =', type(perem_bytes))

print('*******************************')

print('5) Perem_list =', perem_list)
print('Type =', type(perem_list))

print('*******************************')

print('6) Perem_tuple =', perem_tuple)
print('Type =', type(perem_tuple))
print('Perem_tuple =', perem_tuple_2)
print('Type =', type(perem_tuple_2))

print('*******************************')

print('7) Perem_set =', perem_set)
print('Type =', type(perem_set))

print('*******************************')

print('8) Perem_frozenset_0 =', perem_frozenset_0)
print('Type =', type(perem_frozenset_0))
print('Perem_frozenset_1 =', perem_frozenset_1)
print('Type =', type(perem_frozenset_1))

print('*******************************')

print('9) Perem_dict =', perem_dict)
print('Type =', type(perem_dict))

print('*******************************')

#11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
#Конкатенаация — операция склеивания объектов линейной структуры, обычно строк.
perem_1 = 'Course QA'
perem_2 = 'by Vadim Ksendzov'
perem_3 = perem_1 + ' ' + perem_2
print('11)', perem_3)

print('*******************************')

#12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print('12)', perem_str, perem_int)

print('*******************************')

#13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print('13) '+ perem_str + ' ' + str(perem_int))