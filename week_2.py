name_str = input("Введите названия txt. файла без расширения")

with open(f"{name_str}.txt", mode='r') as f:
    word_list = f.readlines()
    clean_word_list = [word_lis.strip().lower().split() for word_lis in word_list]
    our_words = []
    our_words_2 = []
    for i in clean_word_list:
        our_words += i
    for i in our_words:
        if not str(i[-1]).isalpha():
            our_words_2.append(i[:-1])
        elif not str(i[0]).isalpha():
            our_words_2.append(i[1:])
        else:
            our_words_2.append(i)
    our_words_2 = [w for w in our_words_2 if w.strip()]
    a = dict()
    for i in our_words_2:
        if a.get(str(i)) == None:
            a[i] = 1
        else:
            a[i] += 1

spisok = sorted(a.keys())
print(f"В тексте: \n  - всего слов: {len(our_words_2)}; \n  - всего различных слов: {len(spisok)}")
print("Самые часто употребляемые слова в тексте:")
for r,m in a.items():
    if m > len(spisok)/50:
        print(f"{r} : {m} раз употребляется")

    