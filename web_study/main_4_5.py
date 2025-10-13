command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

s_1 = command1.split(' ')
spis_1 = [i for i in s_1 if not i.isalpha()]
out_1 = [x for y in spis_1 for x in y.split(",")] 

s_2 = command2.split(' ')
spis_2 = [i for i in s_2 if not i.isalpha()]
out_2 = [x for y in spis_2 for x in y.split(",")]  

new = set(out_1) & set(out_2)

print(sorted(new))
