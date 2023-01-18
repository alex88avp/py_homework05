# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

def encode(text):
    result = ""
    prev_char = text[0]
    count = 0
    for char in text:
        if char != prev_char:
            result += f'{count}{prev_char}'
            prev_char = char
            count = 1
        else:
            count += 1
    result += f'{count}{prev_char}'
    return result


def decode(text):
    result = ""
    count = ""
    digit = True
    for char in text:
        if digit:
            count = int(char)
            digit = False
        else:
            result += int(count)*char
            digit = True
    return result


text = "AAAAAAFDDCCCCCCCAEEEEEEEE"
print(text)
encode_text = encode(text)
print(encode_text)
print(decode(encode_text))
