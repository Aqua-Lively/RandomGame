import random

print("\n \n \n\n                                                       HELLO THIS IS <<RandomGame>>")
print("Введите от куда до куда загадать мне число и попытайтесь угадать")

res1 = res2 = True
a = b = None

while res1 == True:
   c = None
   exit = True
   while a == None:

      try:
         a = int(input("\nМинимум = "))
      except ValueError:
         print("--------------------------Ошибка(введите число)")
         a = None

   while b == None:

      try:
         b = int(input("\nМаксимум = "))
      except ValueError:
         print("--------------------------Ошибка(введите число)")
         b = None
   if(a > b):
      print("\nа не может быть больше б!")
      a = b = None
   else:
      random_number = random.randint(a,b)
      while c == None:
         c = input("\nУгадай число = ")
         if c in ['x', 'X', 'Exit', 'exit', 'EXIT',]:
            print("\n---------------------------Пока-Пока")
            res1 = False
            c = False
            break
         else:
            try:
               c = int(c)
            except ValueError:
               print("--------------------------Ошибка(введите число)")
               c = None
         if(c != None):
            if c == random_number:
               print("\n----------Вы Угадали!!!!------\n")
               while exit == True:
                  print("Хотите ещё ?\n")
                  answer = input("Введите Да или Нет \n")
                  if answer in ['Да', 'ДА', 'да']:
                     print("---------------------------------------------------------------------------------------------------------")
                     a = b = None
                     exit = False
                  elif answer in ['Нет', 'НЕТ','нет']:
                     res1 = False
                     print("\nПока-Пока :)\n")
                     break
                  else:
                     print("--------------------------Ошибка(Введите 'Да' или  'Нет')")
                     exit == True
            elif(c < random_number):
               print("\n\n---------")
               print("Моё число БОЛЬШЕ!!!")
               print(f'от {a} до {b}')
               print("---------")
               c = None
            elif c > random_number:
               print("\n\n---------")
               print("\nМоё число МЕНЬШЕ!!!")
               print(f'от {a} до {b}')
               print("---------")
               c = None



