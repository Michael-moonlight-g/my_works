ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
spis = ospf_route.replace(',', '').split()
print("{:20} {:20} \n{:20} {:20} \n{:20} {:20} \n{:20} {:20} \n{:20} {:20}".format('Prefix', spis[0], 'AD/Metric', spis[1][1:-1], "Next-Hop",  spis[3], 'Last update', spis[4], 'Outbound Interface', spis[-1]))

# vlan, mac, intf = ['100', 'aabb.cc80.7000', 'Gi0/1']

# print("{:15} {:>15} {:>15}".format(vlan, mac, intf))