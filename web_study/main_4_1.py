nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
word_0 = input("Введите слово из текста: ")
word_1 = input("Введите искомое слово для замены: ")
nat = nat.replace(word_0, word_1)
print(nat)
