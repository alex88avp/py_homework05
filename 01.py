# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".(Задание из семинара)

text = "абв про оооалдд проабв ргшлд оооо абвлгш"
text = text.split()
new_text = []
for i in range(len(text)):
    if "абв" not in text[i]:
        new_text.append(text[i])
print(" ".join(new_text))