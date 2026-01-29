def polindrom(a):
  return a == a[::-1]
stroka = input()
if polindrom(stroka):
  print("Палиндром")
else:
  print("Не палиндром")
