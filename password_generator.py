from random import randint, sample
''' Логика программы: пароль должен состоять из символов 4 типов: буквы верхнего регистра, буквы нижнего регистра, цифры, специальные символы. 
В сумме количество используемых знаков не должно быть менее 12 и одновременно не должно превышать количество знаков, установленное пользователем. 
Из каждого типа знаков программа возьмет рандомное количество знаков. 
При этом количество взятых рандомных значений должно в сумме быть равным количеству знаков, установленному пользователем. 
Тогда - просто навскидку - я делю установленную пользователем длину пароля на 4, как если бы я брала бы поровну из каждого типа: 
если 12 знаков, то на каждый тип по 3 рандомному значению. 
Таким образом, рандомное значение количество знаков из каждого типа будет более 1 (в соответствии с заданием) и не более 3 (это взято навскидку для уравнивания). 
В этом случае программа запрашивает рандомное число от 1 до 3 для каждого из первых трех типов и получает, например, 2 + 1 + 3, 
таким образом для последнего, четвертого типа для приведения к числу 12, программа просто вычитает 6 из 12. 
То есть на выходе получается нужная сумма рандомных количеств из составных частей -  12. 
После этого из каждого типа программа берет по вычисленному соответствующему количеству рандомных значений: из 1 типа - 2, из 2 - 1, из 3 - 3, из 4 - 6. 
'''

# Создаю списки знаков разного типа
# получается 4 составных части пароля (ниже - parts). Умножаю каждый список на 5, чтобы в пароле могли быть повторяющиеся цифры и символы.
chars = '!@#$%^&*()-+' * 5
chars = list(chars)
numbers = '0123456789' * 5
numbers = list(numbers)

# Алфавит умножаю на 5, чтобы в пароле могли быть повторяющиеся буквы
letters_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 5
letters_upper = list(letters_upper)
letters_lower = 'abcdefghijklmnopqrstuvwxyz' * 5
letters_lower = list(letters_lower)

# Запрашиваю пользователя ввести длину пароля. 
# Проверяю, чтобы введенная строка содержала 2 символа,
# чтобы эти символы были числом
# чтобы число было более или равно 12 
   
while True:
  length = input("Введите длину пароля - двузначное число не меньше 12: ")
  if len(length) != 2:
    print("Ввод осуществлен некорректно") 
  else:
    if length.isdigit() == False:
      print("Ввод осуществлен некорректно: необходимо ввести число") 
    else: 
      length = int(length)
      if 30 >= length >= 12:
        print("Супер! Ваш сгенерированный пароль:")
        break
      else:
        print("Паоль должен содержать не менее 12 и не более 30 знаков: ")

# Методом деления выясняю, не более какого количества знаков из каждой составной части parts я могу использовать для пароля, если бы, например, использовала бы равное количество знаков из каждой части
# для учета того, что в сумме количество всех знаков из всех составных частей не может превышать обозначенную длину пароля
        
parts = 4 # количество составных частей (chars, numbers, letters_upper, letters_lower)
quantity_in_1_part = int(length/parts)
#print(quantity_in_1_part)

# Присваиваю каждой составной части (parts) название переменной
# Помещаю в переменные по одному рандомному числу из quantity_in_1_part

quantity_chars = randint(1, quantity_in_1_part) 
#print(quantity_chars)
quantity_numbers = randint(1, quantity_in_1_part) 
#print(quantity_numbers)
quantity_upper = randint(1, quantity_in_1_part) 
#print(quantity_upper)

# Складываю сумму знаков из трех первых составных частей пароля
sum_quantity = quantity_chars + quantity_numbers + quantity_upper

# Четвертую составную часть пароля (quantity_lower) вычисляю как разницу между уже полученной суммой знаков и необходимой объявленной длиной пароля
quantity_lower = length - sum_quantity
#print(quantity_lower)

# Для каждой составной части пароля теперь есть количество знаков, которые рандомно получаю из соответствующей составной части:
random_chars = sample(chars, quantity_chars)
#print(random_chars)
random_numbers = sample(numbers, quantity_numbers)
#print(random_numbers)
random_upper = sample(letters_upper, quantity_upper)
#print(random_upper)
random_lower = sample(letters_lower, quantity_lower)
#print(random_lower)

# Склеиваю рандомные знаки составных частей в один список
password_pilot = random_chars + random_numbers + random_upper + random_lower
#print(password_pilot)

# Перемешиваю знаки в полученном пароле и привожу пароль к строке
password = sample(password_pilot, len(password_pilot))
#print(password)
password = ''.join(password)
print(password)
