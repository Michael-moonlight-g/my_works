word_0, word_1, word_2 = input("Введите три слова через пробел").split()
symbol_0 = input('Введите символ между словами изначальный: ')
symbol_1 = input("Введите символ между словами новый:")
text_0 = word_0 +symbol_0 + word_1 +symbol_0 + word_2
text_1 = text_0.replace(symbol_0, symbol_1)
print(text_1)