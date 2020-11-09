import random
chars = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@$%^&*()_-+"

def gen():
  try:
    length = input("Введите длину пароля >> ")
    res = ""

    for i in range(int(length)):
      res += chars[random.randint(0, len(chars) - 1)]

    print("Пароль: " + res + "\n")
  except:
    print("Ошибка.\n")
    
  gen()

gen()