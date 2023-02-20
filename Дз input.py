x = input("введите свое имя:")
#Пишем имя
print("Привет, ",x)
#Привет, имя
#input

age_str = input("Введите ваш возраст: ")
age = int(age_str)
print(age)
print(type(age))
#input (int)

height = float(input("Укажите свой рост (см): "))
print(height)
print(type(height))
#input (float)

while True:
    user_input = input('Do you like sweet food? True / False: ')
    if user_input.capitalize() == 'True':
        print('ты сладкоежка')
        break
    elif user_input.capitalize() == 'False':
        print('ты не сладкоежка')
        break
    else:
        print('Enter True or False')
        continue
#input (bool)

a = complex(1, 2)
print(a)
b = complex(1, 1.5)
print(b)
c = complex(-1.5, 3.414)
print(c)

#float хранит значения с плавающей запятой, то есть значения, имеющие потенциальные десятичные знаки
#int хранит только целые значения, т.е. целые числа
















