# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(string):
     return string.replace("!", "")

input_string = input("Введите текст: ")
output_string = remove_exclamation_marks(input_string)
print(output_string)


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(string):
  if string.endswith('!'):
        return string[:-1]
  else:
        return string
input_string = input("Введите текст: ")
output_string = remove_last_em(input_string)
print(output_string)