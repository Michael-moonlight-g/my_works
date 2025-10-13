
config = "switchport trunk allowed vlan 1,3,10,20,30,100"

s = config.split(' ')
spis = [i for i in s if not i.isalpha()]
out = [x for y in spis for x in y.split(",")]     #  - №1
# out = spis[0].split(',')                           - №2
print(out)
